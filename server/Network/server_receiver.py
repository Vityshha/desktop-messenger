import socket
import threading
import time

from PyQt6.QtCore import pyqtSignal as Signal, QObject
from server.Network.check_db import CheckThread
from server import server_constant
from server.Network.connect_db import Connect_DB



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
            msg_lenght = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_lenght:
                msg_lenght = int(msg_lenght)
                msg = conn.recv(msg_lenght).decode(self.FORMAT)
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
                    return
                if msg[0:3] == '#!0':
                    self.auth(msg[3:], conn)
                elif msg[0:3] == '#!1':
                    self.reg(msg[3:], addr, conn)
                elif msg[0:3] == '#?0':
                    self.user_db(msg[3:], conn)
                elif msg[0:4] == 'user':
                    print(msg)
                    self.messages_to_db(msg, conn)
                elif msg[0:5] == 'start':
                    self.add_old_user(msg[6:], conn)
                elif msg[0:6] == 'select':
                    self.show_user_sms(msg[7:], conn)
                else:
                    print(msg)
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
            print('Найдено', send_client_text)
            conn.send(send_client_text.encode(self.FORMAT))

    def messages_to_db(self, msg=None, conn=None):
        id = msg.split("user:")[1].split("to:")[0].strip()
        id_send = msg.split("to:")[1].split("#!msg:")[0].strip()
        msg = msg.split("#!msg:")[1].strip()
        self.db_method.messages_db(id, id_send, msg)


    def add_old_user(self, user=None, conn=None):
        request = f'SELECT DISTINCT id_send FROM messages WHERE id = "{str(user)}";'
        users = self.db_method.select_db(request)
        result_string = ', '.join([item[0] for item in users])
        msg = 'user: ' + result_string
        time.sleep(0.5)
        conn.send(msg.encode(self.FORMAT))


    def show_user_sms(self, user=None, conn=None):
        id = user.split("user:")[1].split("user_send:")[0].strip()
        id_send = user.split("user_send:")[1].strip()
        request = f"SELECT message FROM messages WHERE (id = '{str(id)}' AND id_send = '{str(id_send)}')"
        msg = self.db_method.select_db(request)
        try:
            messages = '\n'.join([item[0] for item in msg])
            msg_full = '#!msg_u: ' + messages
            conn.send(msg_full.encode(self.FORMAT))
        except:
            return



