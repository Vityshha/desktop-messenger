import socket
# import pickle ??????????

HEADER = 64
PORT = 5050
SERVER = '172.28.48.1'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))



if __name__ == '__main__':
    msg = 'Hello, world2!'
    send(msg)
    send(DISCONNECT_MESSAGE)
