import socket
import threading
import time

from client.client_constant import Constant
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import QObject


class Sender(QObject):
    signal_authorization_status = Signal()
    signal_authorization_text = Signal(str)
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
            # Добавить повторную отправку на GUI о том что сервак не доступен

    def send_authorization(self, msg):
        if msg:
            message = msg.encode(self.FORMAT)
            msg_lenght = len(message)
            send_lenght = str(msg_lenght).encode(self.FORMAT)
            send_lenght += b' ' * (self.HEADER - len(send_lenght))
            try:
                self.client.send(send_lenght)
                self.client.send(message)
                self.start_listen_server()
            except:
                print('[SEND ERROR] Не авторизовался')

    #Слушаем сервер
    def start_listen_server(self):
        msg = self.client.recv(2048).decode(self.FORMAT)
        if msg:
            if msg == '#!ay':
                self.signal_authorization_status.emit()
                self.client.close()
            elif msg == '#!an':
                self.notification = 'Проверьте введенные данные!'
                self.signal_authorization_text.emit(self.notification)
            elif msg == '#!ry':
                self.notification = 'Успешная регистрация!'
                self.signal_authorization_text.emit(self.notification)
            elif msg == '#!rn':
                self.notification = 'Пользователь уже занят!'
                self.signal_authorization_text.emit(self.notification)
            else:
                self.notification = 'Произошла ошибка!'
                self.signal_authorization_text.emit(self.notification)
                print('Пришло')
