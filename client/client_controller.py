import sys

from GUI.UI_MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, pyqtSignal as Signal

from Network.client_sender import Sender


class Controller(QMainWindow):
    """
    Класс связывающий отображение с моделью
    """
    signa_send_message = Signal(str)

    def __init__(self, isModel=None, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = isModel

        self.sender = Sender()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.init_const()
        self.init_connect()
        self.init_connect_signal()
        self.show()

    def init_connect(self):
        self.ui.btn_close.clicked.connect(self.close_app)
        self.ui.btn_shape.clicked.connect(self.resize_window)
        self.ui.btn_remove.clicked.connect(self.remove_window)
        self.ui.btn_send.clicked.connect(self.send_message)
        self.ui.list_users.clicked.connect(self.user_choise)
        self.ui.btn_settings.clicked.connect(self.setting_mode)


        self.ui.send_text.setPlaceholderText(self.default_sms)
        self.ui.send_text.installEventFilter(self)

        self.ui.search_text.setPlaceholderText(self.default_search)
        self.ui.send_text.installEventFilter(self)

    def init_connect_signal(self):
        self.signa_send_message.connect(self.sender.send)

    def init_const(self):
        self.default_sms = 'Введите собщение...'
        self.default_search = 'Поиск'
        self.default_color = 'color: rgba(79, 91, 103, 0.8); border: transparent;'
        self.select_color = 'color: rgba(255, 255, 255, 1); border: transparent;'
        self.shoise_user = None

    def close_app(self):
        message = '!DISCONNECT'
        self.signa_send_message.emit(message)
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
        self.signa_send_message.emit(message)
        self.ui.send_text.clear()


    def user_choise(self):
        self.shoise_user = self.ui.list_users.currentItem().text()
        self.ui.user_label.setText(self.shoise_user)

    def setting_mode(self):
        print('Окно настроек')


    def put_text_search(self):
        self.ui.search_text.clear()


    #todo доделать пока что хуйня
    def eventFilter(self, source, event):
        if source == self.ui.send_text:
            if event.type() == event.Type.FocusIn:
                self.ui.send_text.setStyleSheet(self.select_color)
                if self.ui.send_text.toPlainText().strip() == self.default_sms:
                    self.ui.send_text.clear()
            elif event.type() == event.Type.FocusOut:
                self.ui.send_text.setStyleSheet(self.default_color)
                if self.ui.send_text.toPlainText().strip() == "":
                    self.ui.send_text.setPlainText(self.default_sms)
        return super().eventFilter(source, event)