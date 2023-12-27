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
    signal_image = Signal(bytes)

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
        self.client.send(b"TEXT")
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
            self.client.send(b"TEXT")
            message = msg.encode(self.FORMAT)
            msg_lenght = len(message)
            send_lenght = str(msg_lenght).encode(self.FORMAT)
            send_lenght += b' ' * (self.HEADER - len(send_lenght))
            try:
                self.client.send(send_lenght)
                self.client.send(message)
            except:
                print('[SEND ERROR] Не авторизовался')

    def send_ico(self, image_path):
        try:
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()

            self.client.send(b"IMAGE")

            image_length = len(image_data)
            send_length = str(image_length).encode(self.FORMAT)
            send_length += b' ' * (self.HEADER - len(send_length))
            self.client.send(send_length)

            self.client.sendall(image_data)

        except Exception as e:
            print('[SEND IMAGE ERROR]', str(e))
            self.notification = 'Ошибка при отправке изображения!'

    def listen_server(self):
        while True:

            try:
                msg_type = self.client.recv(self.HEADER).decode(self.FORMAT)
            except:
                print(f'[CLIETN] Сервер разорвал подключение')
                return

            if msg_type == "IMAGE":
                try:
                    self.client.send("OK".encode(self.FORMAT))
                    image_length = int(self.client.recv(self.HEADER).decode(self.FORMAT))
                    image_data = self.client.recv(image_length)
                    self.signal_image.emit(image_data)
                except:
                    print(f'[CLIENT] Ошибка при приеме изображения')
            else:
                self.process_received_message(msg_type)

    #Слушаем сервер
    def process_received_message(self, msg):
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
            print(msg)
