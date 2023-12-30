import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint, Qt, QEvent
from PyQt5.QtWidgets import QMainWindow
from GUI.UI_Authorization import Ui_Authorization
from PyQt5.QtCore import Qt, pyqtSignal as Signal

class Authorization(QMainWindow):

    signal_send_authorization = Signal(str)
    def __init__(self, parent=None):
        super(Authorization, self).__init__(parent)
        self.ui_authorization = Ui_Authorization()
        self.ui_authorization.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.ui_authorization.btn_reg.clicked.connect(self.reg)
        self.ui_authorization.btn_in.clicked.connect(self.auth)
        self.base_line_edit = [self.ui_authorization.login, self.ui_authorization.password]

        self.init_connect()
        self.installEventFilter(self)
        self.ui_authorization.login.installEventFilter(self)
        self.ui_authorization.password.installEventFilter(self)


    def init_connect(self):
        self.ui_authorization.btn_close.clicked.connect(self.close_app)
        self.ui_authorization.btn_remove.clicked.connect(self.remove_window)


    def auth(self):
        login = self.ui_authorization.login.toPlainText()
        password = self.ui_authorization.password.toPlainText()
        self.signal_send_authorization.emit('#!0 ' + str(login) + ' ' + str(password))

    def reg(self):
        login = self.ui_authorization.login.toPlainText()
        password = self.ui_authorization.password.toPlainText()
        self.signal_send_authorization.emit('#!1 ' + str(login) + ' ' + str(password))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.ui_authorization.widget.geometry().contains(event.pos()):
            self.oldPosition = event.pos()

    def mouseMoveEvent(self, event):
        if self.oldPosition is not None:
            delta = QPoint(event.pos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPosition = None

    def eventFilter(self, obj, event):
        if obj in [self.ui_authorization.login, self.ui_authorization.password] and event.type() == QEvent.KeyPress:
            if event.key() in [Qt.Key_Return, Qt.Key_Enter] and not event.modifiers():
                if self.ui_authorization.login.toPlainText() == '':
                    self.ui_authorization.notif_label.setText('Введите логин!')
                else:
                    if obj is self.ui_authorization.login:
                        self.ui_authorization.password.setFocus()
                        self.ui_authorization.notif_label.setText('')
                    elif self.ui_authorization.password.toPlainText() == '':
                        self.ui_authorization.notif_label.setText('Введите пароль!')
                    else:
                        self.auth()

                return True
        return super().eventFilter(obj, event)

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