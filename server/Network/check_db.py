from PyQt6.QtCore import QThread
from server.database_metod.authorization_db import Authorization
from PyQt6.QtCore import pyqtSignal as Signal

class CheckThread(QThread):

    def __init__(self, data_base_path):
        super(CheckThread, self).__init__()
        self.auth = Authorization(data_base_path)

    def thr_login(self, name, passw):
        self.auth.login(name, passw)

    def thr_register(self, name, passw):
        self.auth.register(name, passw)