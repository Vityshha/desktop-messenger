import sys

from GUI.UI_MainWindow import Ui_MainWindow
from authorization import Authorization

from client_constant import Constant

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal as Signal, QPoint

from Network.client_sender import Sender
from Network.client_receiver import Receiver


class Controller(QMainWindow):
    """
    Класс связывающий отображение c моделью
    """
    signal_send_message = Signal(str)
    signal_search_user = Signal(str)

    def __init__(self, isModel=None, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.client_constant = Constant()
        self.sender = Sender()
        self.send_port = self.sender.port_res
        # self.receiver = Receiver(self.send_port)

        self.login_messager()

        self.model = isModel



    def login_messager(self):
        if self.client_constant.AUTHORIZED == 'True':
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            self.init_const()
            self.init_connect()
            self.show()
            self.signal_send_message.connect(self.sender.send_message)

        else:
            self.Authorization = Authorization()
            self.Authorization.show()
            paragraph = 'Authentication parameters'
            value = 'AUTHORIZED'
            importance = 'True'
            # self.client_constant.shanges(paragraph, value, importance)
            self.Authorization.signal_send_authorization.connect(self.sender.send_authorization)


    def init_connect(self):
        self.ui.btn_close.clicked.connect(self.close_app)
        self.ui.btn_shape.clicked.connect(self.resize_window)
        self.ui.btn_remove.clicked.connect(self.remove_window)
        self.ui.btn_send.clicked.connect(self.send_message)
        self.ui.list_users.clicked.connect(self.user_choise)
        self.ui.btn_settings.clicked.connect(self.setting_mode)

    def init_const(self):
        self.default_sms = 'Введите собщение...'
        self.default_search = 'Поиск'
        self.default_color = 'color: rgba(79, 91, 103, 0.8); border: transparent;'
        self.select_color = 'color: rgba(255, 255, 255, 1); border: transparent;'
        self.shoise_user = None

    def close_app(self):
        message = '!DISCONNECT'
        self.signal_send_message.emit(message)
        self.close()
        sys.exit()

    def resize_window(self):
        if not self.isFullScreen():
            self.showFullScreen()
        else:
            self.showNormal()

    def remove_window(self):
        self.showMinimized()


    def send_message(self):
        message = str(self.ui.send_text.toPlainText())
        if message == '':
            return
        self.signal_send_message.emit(message)
        self.ui.send_text.clear()

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            print('enter')
            message = str(self.ui.send_text.toPlainText())
            if message == '':
                return
            self.signal_send_message.emit(message)
            self.ui.send_text.clear()


    def send_sears_users(self):
        print('Отправка на сервак для поиска usera')


    def user_choise(self):
        self.shoise_user = self.ui.list_users.currentItem().text()
        self.ui.user_label.setText(self.shoise_user)

    def setting_mode(self):
        print('Окно настроек')


    def put_text_search(self):
        self.ui.search_text.clear()


    def mousePressEvent(self, event):
        self.oldPosition = event.pos()

    def mouseMoveEvent(self, event):
        # Move window
        delta = QPoint(event.pos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        # Resize window
