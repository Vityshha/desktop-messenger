from GUI.UI_MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QPoint


class Controller(QMainWindow):
    """
    Класс связывающий отображение с моделью
    """
    def __init__(self, isModel=None, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = isModel

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.init_const()
        self.init_connect()
        self.show()

    def init_connect(self):
        self.ui.btn_close.clicked.connect(self.close_app)
        self.ui.btn_shape.clicked.connect(self.resize_window)
        self.ui.btn_remove.clicked.connect(self.remove_window)
        self.ui.btn_send.clicked.connect(self.send_message)
        self.ui.list_users.clicked.connect(self.user_choise)
        self.ui.btn_settings.clicked.connect(self.setting_mode)
        self.ui.send_text.selectionChanged.connect(self.put_text_sms)
        self.ui.search_text.selectionChanged.connect(self.put_text_search)

    def init_const(self):
        self.flag_resize = True
        self.window_width = None
        self.window_height = None
        self.shoise_user = None

    def close_app(self):
        self.close()

    def resize_window(self):
        if self.flag_resize:
            self.window_width = self.size().width()
            self.window_height = self.size().height()
            self.showFullScreen()
            self.flag_resize = False
        else:
            self.resize(self.window_width,  self.window_height)
            # self.move(0, 0)
            self.flag_resize = True

    def remove_window(self):
        self.showMinimized()


    def send_message(self):
        print(self.ui.send_text.toPlainText())
        self.ui.send_text.clear()


    def user_choise(self):
        self.shoise_user = self.ui.list_users.currentItem().text()
        self.ui.user_label.setText(self.shoise_user)

    def setting_mode(self):
        print('Окно настроек')

    def put_text_sms(self):
        self.ui.send_text.clear()

    def put_text_search(self):
        self.ui.search_text.clear()
