import socket
import threading
import time

from client.client_constant import Constant
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import QObject

class Sender(QObject):
    signal_authorization_status = Signal()
    signal_authorization_text = Signal(str)
    signal_sears_user_bd = Signal(str)
    signal_add_users = Signal(str)
    signal_db_messages = Signal(str)

    def __init__(self):
        super(Sender, self).__init__()
        self.FORMAT = Constant().FORMAT
        self.HEADER = int(Constant().HEADER)
        self.SERVER = Constant().SERVER
        self.PORT = int(Constant().PORT)
        self.ADDR = (self.SERVER, self.PORT)
        self.id = Constant().id
        self.authorization_status = None

        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.ADDR)
        except:
            print('[SEND ERROR] Сервер недоступен')

        self.listen_thread = threading.Thread(target=self.listen_server)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def send_message(self, msg):
        message = msg.encode(self.FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(self.FORMAT)
        send_lenght += b' ' * (self.HEADER - len(send_lenght))
        try:
            self.client.send(send_lenght)
            self.client.send(message)
        except:
            print('[SEND ERROR] Не отправил')
            self.notification = 'Сервер недоступен!'
            self.signal_authorization_text.emit(self.notification)

    def send_authorization(self, msg):
        if msg:
            message = msg.encode(self.FORMAT)
            msg_lenght = len(message)
            send_lenght = str(msg_lenght).encode(self.FORMAT)
            send_lenght += b' ' * (self.HEADER - len(send_lenght))
            try:
                self.client.send(send_lenght)
                self.client.send(message)
            except:
                print('[SEND ERROR] Не авторизовался')

    def send_ico(self, icon):
        file = icon
        image_data = file.read(2048)

        while image_data:
            self.client.send(image_data)
            image_data = file.read(2048)
        file.close()

    def listen_server(self):
        while True:
            try:
                msg = self.client.recv(2048).decode(self.FORMAT)
                if not msg:
                    break
                self.process_received_message(msg)
            except Exception as e:
                print('[LISTEN ERROR]', str(e))
                break

    #Слушаем сервер
    def process_received_message(self, msg):
        print(msg)
        if msg == '#!ay':
            self.signal_authorization_status.emit()
        elif msg == '#!an':
            self.notification = 'Проверьте введенные данные!'
            self.signal_authorization_text.emit(self.notification)
        elif msg == '#!ry':
            self.notification = 'Успешная регистрация!'
            self.signal_authorization_text.emit(self.notification)
        elif msg == '#!rn':
            self.notification = 'Пользователь уже занят!'
            self.signal_authorization_text.emit(self.notification)
        elif msg[:3] == '#?1':
            user = str(msg[5:-3])
            self.signal_sears_user_bd.emit(user)
        elif msg[:4] == 'user':
            user = msg[6:]
            time.sleep(1)
            self.signal_add_users.emit(user)
        elif msg[:7] == '#!msg_u':
            messages = msg[9:]
            self.signal_db_messages.emit(messages)
        else:
            print('[LISTEN ERROR] Проверьте что пришло')
