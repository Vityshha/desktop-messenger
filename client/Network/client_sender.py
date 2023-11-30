import socket
# import pickle ??????????

#todo HEADER слишком большой наверное
HEADER = 64
PORT = 5050
SERVER = '172.30.128.1'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

class Sender():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
    except:
        print('[SEND ERROR] Сервер недоступен')

    def send_message(self, msg):
        message = msg.encode(FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(FORMAT)
        send_lenght += b' ' * (HEADER - len(send_lenght))
        try:
            self.client.send(send_lenght)
            self.client.send(message)
        except:
            print('[SEND ERROR] Сервер недоступен')
            # Добавить повторную отправку на GUI о том что сервак не доступен

    def send_authorization(self, msg):
        message = msg.encode(FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(FORMAT)
        send_lenght += b' ' * (HEADER - len(send_lenght))
        try:
            self.client.send(send_lenght)
            self.client.send(message)
        except:
            print('[SEND ERROR] Сервер недоступен')

    def search_users(self, user):
        print(f'Поиск usera {user}')