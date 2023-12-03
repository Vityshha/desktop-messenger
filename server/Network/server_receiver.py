import socket
import threading

from PyQt6.QtCore import pyqtSignal as Signal, QObject
from server.Network.check_db import CheckThread
from server import server_constant


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
        login = data[0]
        passw = data[1]
        self.check_db.thr_login(login, passw)
        if self.check_db.auth.correct == 0:
            print('norm')
            conn.send(('#!y').encode(self.FORMAT))
        else:
            conn.send(('#!n').encode(self.FORMAT))
            print('ne norm')

    def reg(self, msg, ip, conn):
        data = msg.split()
        login = data[0]
        passw = data[1]
        self.check_db.thr_register(login, passw, ip)
        if self.check_db.auth.correct == 0:
            print('norm')
            conn.send(('#!y').encode(self.FORMAT))
        else:
            print('ne norm')
            conn.send(('#!n').encode(self.FORMAT))