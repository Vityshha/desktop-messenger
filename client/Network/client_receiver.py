import socket
import threading

from PyQt6.QtCore import Qt, pyqtSignal as Signal, QObject

HEADER = 64
PORT = 5051
SERVER = '172.30.128.1'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'


class Receiver(QObject):

    def __init__(self):
        super(Receiver, self).__init__()

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)

    def handle_client(self, conn, addr):

        connected = True
        while connected:
            msg_lenght = conn.recv(HEADER).decode(FORMAT)
            if msg_lenght:
                msg_lenght = int(msg_lenght)
                msg = conn.recv(msg_lenght).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    return
                print(msg)
        conn.close()


    def start(self):
        self.server.listen()
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()


if __name__ == '__main__':
    rec = Receiver()
    rec.start()
