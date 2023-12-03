import socket
import threading
from client.client_constant import Constant
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import QObject

class Sender(QObject):
    signal_authorization_status = Signal()
    signal_authorization_text = Signal(str)
    signal_sears_user_bd = Signal(str)

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
        self.listen_thread.daemon = True  # Поток будет завершен, когда основной поток завершится
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
            except:
                print('[SEND ERROR] Не авторизовался')

    def listen_server(self):
        while True:
            try:
                msg = self.client.recv(2048).decode(self.FORMAT)
                if not msg:
                    break  # Если соединение закрыто, выходим из цикла
                self.process_received_message(msg)
            except Exception as e:
                print('[LISTEN ERROR]', str(e))
                break

    #Слушаем сервер
    def process_received_message(self, msg):
        # Ваш код обработки полученного сообщения
        # Например, вы можете использовать сигналы для обновления GUI
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
            print('Найден пользователь', msg[5:-3])
            user = str(msg[5:-3])
            self.signal_sears_user_bd.emit(user)
        else:
            self.notification = 'Произошла ошибка!'
            self.signal_authorization_text.emit(self.notification)
            print('Пришло', msg)
