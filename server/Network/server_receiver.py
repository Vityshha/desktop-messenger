import socket
import threading
import time
import datetime
import os

from PyQt5.QtCore import pyqtSignal as Signal, QObject
from server.Network.check_db import CheckThread
from server import server_constant
from server.database_metod.database.connect_db import Connect_DB



class Receiver(QObject):

    signal_auth = Signal(str)
    signal_reg = Signal(str)
    signal_message = Signal(str)

    def __init__(self, database):
        super(Receiver, self).__init__()
        self.init_const()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.database = database
        self.check_db = CheckThread(self.database)
        self.db_method = Connect_DB(self.database)



    def init_const(self):
        self.HEADER = int(server_constant.HEADER)
        self.PORT = int(server_constant.PORT)
        self.SERVER = server_constant.SERVER
        self.ADDR = server_constant.ADDR
        self.FORMAT = str(server_constant.FORMAT)
        self.DISCONNECT_MESSAGE = str(server_constant.DISCONNECT_MESSAGE)

    def handle_client(self, conn, addr):
        print(f'[NEW CONNECTIONS] {addr} connected')

        connected = True
        while connected:

            try:
                msg_type = conn.recv(self.HEADER).decode(self.FORMAT)
            except:
                print(f'[CLIETN] Клиент {addr} разорвал подключение')
                return

            if msg_type == "IMAGE":
                try:
                    image_length = int(conn.recv(self.HEADER).decode(self.FORMAT))
                    image_data = conn.recv(image_length)
                    self.db_method.load_icon(image_data, addr)
                except:
                    print(f'[CLIENT] Ошибка при приеме изображения от {addr}')

            elif msg_type == "TEXT":
                try:
                    msg_lenght = conn.recv(self.HEADER).decode(self.FORMAT)
                except:
                    print(f'[CLIETN] Клиент {addr} разорвал подключение')
                    return
                if msg_lenght:
                    msg_lenght = int(msg_lenght)
                    msg = conn.recv(msg_lenght).decode(self.FORMAT)
                else:
                    return

                if msg[0:6] == '#!info':
                    if msg[7:18] == self.DISCONNECT_MESSAGE:
                        self.activ_disconnect_user(msg[19:])
                        connected = False
                        conn.close()
                        return
                    elif msg[7:15] == '!RESTART':
                        print('RESTART ', msg[16:])
                        self.activ_disconnect_user(msg[16:])
                    else:
                        print(msg)
                elif msg[0:3] == '#!0':
                    self.auth(msg[3:], conn)
                elif msg[0:3] == '#!1':
                    self.reg(msg[3:], addr, conn)
                elif msg[0:3] == '#?0':
                    self.user_db(msg[3:], conn)
                elif msg[0:4] == 'user':
                    self.messages_to_db(msg, conn)
                elif msg[0:5] == 'start':
                    self.add_old_user(msg[6:], addr, conn)
                elif msg[0:6] == 'select':
                    self.show_user_sms(msg[7:], conn)
                else:
                    print(f'Непонятное смс {msg}')
        conn.close()

    def start(self):
        self.server.listen()
        print(f'[LISTENING] Server is listening on {self.SERVER}')
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

    def auth(self, msg, conn):
        data = msg.split()
        if data == []:
            return
        login = data[0]
        passw = data[1]
        self.check_db.thr_login(login, passw)
        if self.check_db.auth.correct == 0:
            conn.send(('#!ay').encode(self.FORMAT))
        else:
            conn.send(('#!an').encode(self.FORMAT))

    def reg(self, msg, ip, conn):
        data = msg.split()
        if data == []:
            return
        login = data[0]
        passw = data[1]
        self.check_db.thr_register(login, passw, ip)
        if self.check_db.auth.correct == 0:
            conn.send(('#!ry').encode(self.FORMAT))
        else:
            conn.send(('#!rn').encode(self.FORMAT))

    def user_db(self, user=None, conn=None):
        request = f'SELECT login FROM users WHERE login = "{user}"'
        user = self.db_method.select_db(request)
        send_client_text = '#?1' + str(user)[1:-1]
        if send_client_text == '#?1':
            return
        else:
            conn.send(send_client_text.encode(self.FORMAT))

    def messages_to_db(self, msg=None, conn=None):
        #Вот тут можно смотреть в сети он или нет и сразу отправлтяь уведомления об этом.
        #Если не в сети, то просто в бд и потом при входе говорить что есть новые смс
        id = msg.split("user:")[1].split("to:")[0].strip()
        id_send = msg.split("to:")[1].split("#!msg:")[0].strip()
        msg = msg.split("#!msg:")[1].strip()
        try:
            self.db_method.messages_db(id, id_send, msg)
        except:
            print(f'[BD ERROR] Ошибка добавления сообщения в БД')


    def add_old_user(self, user=None, addr=None, conn=None):
        request = f'SELECT DISTINCT id_send FROM messages WHERE id = "{str(user)}" UNION SELECT DISTINCT id FROM messages WHERE id_send = "{str(user)}";'
        # try:
        users = self.db_method.select_db(request)
        result_string = ', '.join([item[0] for item in users])
        if result_string == '':
            return
        msg = 'user: ' + result_string
        conn.send(msg.encode(self.FORMAT))

        request = f'UPDATE users SET activ = 1 WHERE login = "{str(user)}";'
        self.db_method.select_db(request)
        request = f'UPDATE users SET addres = "{str(addr)}" WHERE login = "{str(user)}";'
        self.db_method.select_db(request)

        request = f"SELECT icon FROM users WHERE login = '{user}'"
        user_icon_path = self.db_method.select_db(request)[0][0]
        self.send_icon_client(user_icon_path, conn)

    def show_user_sms(self, user=None, conn=None):
        id = user.split("user:")[1].split("user_send:")[0].strip()
        id_send = user.split("user_send:")[1].strip()
        request = f"SELECT id, id_send, message, time_sms, read  FROM messages WHERE ((id = '{str(id)}' AND id_send = '{str(id_send)}') OR (id = '{str(id_send)}' AND id_send = '{str(id)}'));"
        # try:
        msg = self.db_method.select_db(request)
        msg_full = '#!msg_u: ' + str(msg)
        conn.send(msg_full.encode(self.FORMAT))

        confirmation = conn.recv(self.HEADER).decode(self.FORMAT)
        print('Подтверждение от клиента')
        if confirmation == "OK":
            request = f"SELECT activ, time_activ FROM users WHERE login = '{str(id_send)}';"
            activ = self.db_method.select_db(request)
            msg_full = '#!msg_a: ' + str(activ)
            conn.send(msg_full.encode(self.FORMAT))

        request = f'UPDATE messages SET read = 1 WHERE id_send = "{str(id)}";'
        self.db_method.select_db(request)
        # except:
        #     print(f'[BD ERROR] Ошибка поиска сообщений в БД')

    def activ_disconnect_user(self, login):
        request = f"UPDATE users SET activ = 0 WHERE login = '{login}'"
        self.db_method.update_db(request)

        time_last_connect = str(datetime.datetime.now())
        request = f"UPDATE users SET time_activ = '{time_last_connect}' WHERE login = '{login}'"
        self.db_method.update_db(request)


    def send_icon_client(self, path, conn):
        try:
            if path is None:
                return
            if os.path.exists(path):
                with open(path, 'rb') as image_file:
                    image_data = image_file.read()
            else:
                print(f"Файл {path} не существует.")
                return

            conn.send(b"IMAGE")

            confirmation = conn.recv(self.HEADER).decode(self.FORMAT)
            print('Подтверждение от клиента')
            if confirmation == "OK":
                image_length = len(image_data)
                send_length = str(image_length).encode(self.FORMAT)
                send_length += b' ' * (self.HEADER - len(send_length))

                conn.send(send_length)

                conn.sendall(image_data)

        except Exception as e:
            print('[SEND IMAGE ERROR]', str(e))
