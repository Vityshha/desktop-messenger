import socket
import threading

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal as Signal, QObject
from server.Network.check_db import CheckThread
from server.Network.server_sender import Sender

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'



class Receiver(QObject):

    signal_auth = Signal(str)
    signal_reg = Signal(str)
    signal_message = Signal(str)

    def __init__(self, database):
        super(Receiver, self).__init__()

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)
        self.database = database
        self.check_db = CheckThread(self.database)


    def handle_client(self, conn, addr):
        print(f'[NEW CONNECTIONS] {addr} connected')

        connected = True
        while connected:
            self.sender = Sender(addr)
            msg_lenght = conn.recv(HEADER).decode(FORMAT)
            if msg_lenght:
                msg_lenght = int(msg_lenght)
                msg = conn.recv(msg_lenght).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    return
                print(f'[{addr}] [{msg[0:3]}] {msg[3:]}')
                if msg[0:3] == '#!0':
                    self.auth(msg[3:])
                elif msg[0:3] == '#!1':
                    self.reg(msg[3:], ip=addr)
                else:
                    print('хз пришло')
        conn.close()

    def start(self):
        self.server.listen()
        print(f'[LISTENING] Server is listening on {SERVER}')
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

    def auth(self, msg):
        data = msg.split()
        login = data[0]
        passw = data[1]
        self.check_db.thr_login(login, passw)

    def reg(self, msg, ip):
        data = msg.split()
        login = data[0]
        passw = data[1]
        self.check_db.thr_register(login, passw, ip)
        self.check_db.auth.correct = 0
        self.correct_authorization()


    def correct_authorization(self):
        print('Отправка сигнала о правильном вхлде')
        self.sender.client_send_message(msg='correct')
