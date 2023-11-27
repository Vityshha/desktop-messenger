import socket
# import pickle ??????????
from PyQt6.QtCore import pyqtSlot as Slot, pyqtSignal as Signal

HEADER = 64
PORT = 5050
SERVER = '172.29.80.1'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

class Sender():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
    except:
        print("Сервак не запущен")

    def send(self, msg):
        message = msg.encode(FORMAT)
        print(message.decode(FORMAT))
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(FORMAT)
        send_lenght += b' ' * (HEADER - len(send_lenght))
        try:
            self.client.send(send_lenght)
            self.client.send(message)
            print(self.client.recv(2048).decode(FORMAT))
        except:
            print("Сервак не запущен")


# if __name__ == '__main__':
#     msg = 'Hello, world2!'
#     send(msg)
#     send(DISCONNECT_MESSAGE)
