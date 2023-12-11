import sys
import time

from GUI.UI_MainWindow import Ui_MainWindow
from authorization import Authorization
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal as Signal, pyqtSlot as Slot, QPoint, QObject
from Network.client_sender import Sender
from client_constant import Constant
import re


class Controller(QMainWindow):
    signal_send_message = Signal(str)
    signal_search_user = Signal(str)

    def __init__(self, isModel=None, parent=None):
        super(Controller, self).__init__(parent)
        self.client_constant = Constant()
        self.sender = Sender()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.init_const()
        self.Authorization = Authorization()
        self.model = isModel
        self.login_messager()
        self.init_connect()
        self.flag_sms = True




    def login_messager(self):
        if self.client_constant.AUTHORIZED == 'True':
            self.show()
        else:
            self.Authorization.show()

    def search_user(self):
        text = '#?0' + self.ui.search_text.toPlainText()
        self.signal_search_user.emit(text)

    def authorization_close(self):
        self.Authorization.close()
        paragraph = 'Authentication parameters'
        value = 'AUTHORIZED'
        importance = 'True'
        login = self.Authorization.ui_authorization.login.toPlainText()
        password = self.Authorization.ui_authorization.password.toPlainText()
        self.client_constant.shanges(paragraph, value, importance)

        self.client_constant.shanges(paragraph, 'login', login)
        self.client_constant.shanges(paragraph, 'password', password)
        self.show()


    def init_connect(self):
        self.ui.btn_close.clicked.connect(self.close_app)
        self.ui.btn_shape.clicked.connect(self.resize_window)
        self.ui.btn_remove.clicked.connect(self.remove_window)
        self.ui.btn_send.clicked.connect(self.send_message)
        self.ui.list_users.clicked.connect(self.user_choise)
        self.ui.btn_settings.clicked.connect(self.setting_mode)

        self.signal_send_message.connect(self.sender.send_message)
        self.Authorization.signal_send_authorization.connect(self.sender.send_authorization)
        self.sender.signal_authorization_status.connect(self.authorization_close)
        self.sender.signal_authorization_text.connect(self.notification_author)
        self.ui.search_text.textChanged.connect(self.search_user)
        self.signal_search_user.connect(self.sender.send_authorization)
        self.sender.signal_sears_user_bd.connect(self.user_add)

        self.sender.signal_add_users.connect(self.user_add_db)
        self.sender.signal_db_messages.connect(self.add_messages)


    def init_const(self):
        self.default_sms = 'Введите собщение...'
        self.default_search = 'Поиск'
        self.default_color = 'color: rgba(79, 91, 103, 0.8); border: transparent;'
        self.select_color = 'color: rgba(255, 255, 255, 1); border: transparent;'
        self.shoise_user = None

    @Slot(str)
    def notification_author(self, notif):
        self.Authorization.ui_authorization.notif_label.setText(notif)

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

    @Slot(str)
    def user_add(self, user):
        self.books = []
        for i in range(self.ui.list_users.count()):
            book = self.ui.list_users.item(i).text()
            self.books.append(book)
        if user in self.books:
            return
        else:
            self.ui.list_users.addItem(user)

    @Slot(str)
    def user_add_db(self, users):
        users = users.split(', ')
        for user in users:
            self.ui.list_users.addItem(user)

    @Slot(str)
    def add_messages(self, messages):
        messages = messages[1:-1]
        result = re.findall(r'\((.*?)\)', messages)
        ite = [item.replace("'", "") for item in result]
        ite = [item.split(', ') for item in ite]
        messages = ''
        for itt in ite:
            if itt[0] == self.client_constant.login:
                messages += f"<div style='text-align:right;'>{itt[2]}</div>" + '\n'
            else:
                messages += f"<div style='text-align:left;'>{itt[2]}</div>" + '\n'
        self.ui.sms_label.setText(messages)
        self.flag_sms = not self.flag_sms


    def send_message(self):
            msg = str(self.ui.send_text.toPlainText())
            try:
                user_send = self.ui.list_users.currentItem().text()
            except:
                return
            if msg == '' or user_send == '':
                return
            else:
                message = f'user: {self.client_constant.login} ' + 'to: ' + user_send + ' #!msg: ' + msg
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


    def user_choise(self):
        self.shoise_user = self.ui.list_users.currentItem().text()
        self.ui.user_label.setText(self.shoise_user)
        msg = 'select: ' + 'user: ' + self.client_constant.login + ' user_send: ' + self.shoise_user
        self.signal_send_message.emit(msg)

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
