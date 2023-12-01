from server.Network.connect_db import Connect_DB
import socket

FORMAT = 'utf-8'
HEADER = 64
class Sender():

    def __init__(self, ADDR=None):
        self.ADDR = ADDR
        print('Пытаюсь подключиться к ', ADDR)

        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.connect(self.ADDR)
        except:
            print('Клиент недоступен')

    def client_send_message(self, msg):
        message = msg.encode(FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(FORMAT)
        send_lenght += b' ' * (HEADER - len(send_lenght))
        try:
            self.server.send(send_lenght)
            self.server.send(message)
        except:
            print('Клиент недоступен')


