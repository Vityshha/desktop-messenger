import os
import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'