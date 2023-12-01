import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QMainWindow
from GUI.UI_Authorization import Ui_Authorization
from PyQt5.QtCore import Qt, pyqtSignal as Signal

class Authorization(QMainWindow):

    signal_send_authorization = Signal(str)
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui_authorization = Ui_Authorization()
        self.ui_authorization.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.ui_authorization.btn_reg.clicked.connect(self.reg)
        self.ui_authorization.btn_in.clicked.connect(self.auth)
        self.base_line_edit = [self.ui_authorization.login, self.ui_authorization.password]

        self.init_connect()


    def init_connect(self):
        self.ui_authorization.btn_close.clicked.connect(self.close_app)
        self.ui_authorization.btn_remove.clicked.connect(self.remove_window)


    #Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def auth(self):
        login = self.ui_authorization.login.toPlainText()
        password = self.ui_authorization.password.toPlainText()
        print(f'Проверка в БД {login}, {password}')
        self.signal_send_authorization.emit('#!0 ' + str(login) + ' ' + str(password))

    def reg(self):
        login = self.ui_authorization.login.toPlainText()
        password = self.ui_authorization.password.toPlainText()
        print(f'Запись в БД {login}, {password}')
        self.signal_send_authorization.emit('#!1 ' +str(login) + ' ' + str(password))

    def mousePressEvent(self, event):
        self.oldPosition = event.pos()

    def mouseMoveEvent(self, event):
        # Move window
        delta = QPoint(event.pos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        # Resize window

    def close_app(self):
        message = '!DISCONNECT'
        self.signal_send_authorization.emit(message)
        self.close()
        sys.exit()

    def remove_window(self):
        self.showMinimized()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Authorization()
    win.show()
    sys.exit(app.exec())