import socket
import threading

from PyQt5.QtCore import Qt, pyqtSignal as Signal, QObject

HEADER = 64
PORT = 5051
SERVER = '192.168.50.133'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'


class Receiver(QObject):

    def __init__(self, port):
        super(Receiver, self).__init__()
        print(port, 123)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (SERVER, port+1)
        self.server.bind(ADDR)
        port_res = self.server.getsockname()[1]
        print(port_res)

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
