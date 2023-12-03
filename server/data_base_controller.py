from server.Network.connect_db import Connect_DB
from Network.server_receiver import Receiver


class DataBaseController:
    def __init__(self, database):
        self.database = database
        self.db_method = Connect_DB(self.database)
        self.receiver = Receiver(self.database)

        self.receiver.start()




if __name__ == '__main__':
    database = 'C:\\Users\\KFU\\Desktop\\desktop-messenger\\server\\database_metod\\database\\users.db'
    db_c = DataBaseController(database)
    # db_c.receiver.start()