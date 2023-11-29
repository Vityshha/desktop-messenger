import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from GUI.UI_Authorization import Ui_Authorization
from check_db import *

class Authorization(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui_authorization = Ui_Authorization()
        self.ui_authorization.setupUi(self)

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

        self.ui_authorization.btn_reg.clicked.connect(self.reg)
        self.ui_authorization.btn_in.clicked.connect(self.auth)
        self.base_line_edit = [self.ui_authorization.login, self.ui_authorization.password]

    #декоратор проверки правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.toPlainText()) == 0:
                    return
            funct(self)
        return wrapper

    #Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    # @check_input
    def auth(self):
        login = self.ui_authorization.login.toPlainText()
        password = self.ui_authorization.password.toPlainText()
        self.check_db.thr_login(login, password)

    # @check_input
    def reg(self):
        login = self.ui_authorization.login.toPlainText()
        password = self.ui_authorization.password.toPlainText()
        self.check_db.thr_register(login, password)
        print(self.check_db.thr_register)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Authorization()
    win.show()
    sys.exit(app.exec())