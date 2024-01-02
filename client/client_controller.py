import sys
import datetime

from PyQt5.QtGui import QPixmap, QImage, QBrush, QPainter, QWindow, QIcon

from Custom_Widgets import loadJsonStyle
from GUI.UI_MainWindow import Ui_MainWindow
from authorization import Authorization
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QGraphicsBlurEffect, QGridLayout, QLabel
from PyQt5.QtCore import Qt, pyqtSignal as Signal, pyqtSlot as Slot, QPoint, QEvent, QRect, QSize, QByteArray, QBuffer, \
    QIODevice
from Network.client_sender import Sender
from client_constant import Constant
import re


class Controller(QMainWindow):
    signal_send_message = Signal(str)
    signal_search_user = Signal(str)

    def __init__(self, isModel=None, parent=None):
        super(Controller, self).__init__(parent)
        self.sender = Sender()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.init_const()
        self.Authorization = Authorization()
        self.model = isModel
        self.login_messager()
        self.init_connect()


    def login_messager(self):
        if Constant().AUTHORIZED == 'True':
            self.show()
            start_msg = 'start ' + Constant().login
            self.sender.send_message(start_msg)
            self.menu_bar_settings()
        else:
            self.Authorization.show()

    def search_user(self):
        text = '#?0' + self.ui.search_text.toPlainText()
        self.func_textchanged()
        self.signal_search_user.emit(text)


    def func_textchanged(self):
        if self.ui.list_users.count() == 0:
            return
        if self.ui.search_text.toPlainText() == '':
            for i in range(self.ui.list_users.count()):
                self.ui.list_users.takeItem(0)
            for i in range(len(self.original_items)):
                self.ui.list_users.addItem(self.original_items[i])

        search_text = self.ui.search_text.toPlainText().lower()
        item_anywhere = self.ui.list_users.findItems(search_text, Qt.MatchContains)

        start_list = list(filter(lambda item: item.text().lower().startswith(search_text), item_anywhere))
        start_text = [x.text().lower() for x in start_list]

        def bw_filter(item):
            item_text = item.text().lower()
            return search_text in item_text[1:-1] and item_text not in start_text

        bw_lst = list(filter(bw_filter, item_anywhere))
        bw_lst.sort(key=lambda item: item.text().lower().find(search_text))
        bw_text = [x.text().lower() for x in bw_lst]

        def end_filter(item):
            item_text = item.text().lower()
            return item_text.endswith(search_text) and item_text.lower() not in start_text and item_text not in bw_text

        end_lst = list(filter(end_filter, item_anywhere))
        end_lst.sort(key=lambda item: item.text().lower().find(search_text))


        for i in range(self.ui.list_users.count()):
            self.ui.list_users.takeItem(0)

        for item in start_list + bw_lst + end_lst:
            self.ui.list_users.addItem(item.text())

        for i in range(len(self.original_items)):
            item_text = self.original_items[i]
            existing_items = self.ui.list_users.findItems(item_text, Qt.MatchExactly)
            if not existing_items:
                self.ui.list_users.addItem(item_text)
            else:
                pass


    def authorization_close(self):
        self.Authorization.close()
        paragraph = 'Authentication parameters'
        value = 'AUTHORIZED'
        importance = 'True'
        login = self.Authorization.ui_authorization.login.toPlainText()
        password = self.Authorization.ui_authorization.password.toPlainText()
        Constant().shanges(paragraph, value, importance)

        Constant().shanges(paragraph, 'login', login)
        Constant().shanges(paragraph, 'password', password)
        self.show()
        start_msg = 'start ' + login
        self.sender.send_message(start_msg)

        self.menu_bar_settings()


    def init_connect(self):
        self.ui.btn_close.clicked.connect(self.close_app)
        self.ui.btn_shape.clicked.connect(self.resize_window)
        self.ui.btn_remove.clicked.connect(self.remove_window)
        self.ui.btn_send.clicked.connect(self.send_message)
        self.ui.list_users.clicked.connect(self.user_choise)
        self.ui.scrollArea.verticalScrollBar().rangeChanged.connect(self.scrollToBottom)

        self.signal_send_message.connect(self.sender.send_message)
        self.Authorization.signal_send_authorization.connect(self.sender.send_authorization)
        self.sender.signal_authorization_status.connect(self.authorization_close)
        self.sender.signal_authorization_text.connect(self.notification_author)
        self.ui.search_text.textChanged.connect(self.search_user)
        self.signal_search_user.connect(self.sender.send_authorization)
        self.sender.signal_sears_user_bd.connect(self.user_add)

        self.sender.signal_add_users.connect(self.user_add_db)
        self.sender.signal_db_messages.connect(self.add_messages)
        self.sender.signal_activ.connect(self.show_activ_user)

        self.sender.signal_image.connect(self.client_image)

        self.ui.send_text.installEventFilter(self)
        self.installEventFilter(self)

        self.ui.btn_settings.clicked.connect(self.effects)

    def init_const(self):
        self.shoise_user = None
        self.ui.send_text.setAcceptRichText(False)
        self.ui.stackedWidget_sms.setCurrentIndex(1)
        self.menu_bar_settings()
        loadJsonStyle(self, self.ui, jsonFiles={"GUI\style.json"})
        self.blur_effect = QGraphicsBlurEffect()
        self.ui.widget_right_main.setGraphicsEffect(self.blur_effect)
        self.blur_effect.setEnabled(False)
        self.ui.app_text.setText('<a href="https://github.com/Vityshha/desktop-messenger/tree/main" style="color: white; text-decoration: none;">KFU Desktop Messaging</a>')

    @Slot(str)
    def notification_author(self, notif):
        self.Authorization.ui_authorization.notif_label.setText(notif)

    def close_app(self):
        message = '#!info ' + '!DISCONNECT ' + Constant().login
        self.signal_send_message.emit(message)
        self.close()
        self.thread().quit()
        sys.exit()


    def resize_window(self):
        if not self.isFullScreen():
            self.showFullScreen()
        else:
            self.showNormal()

    def remove_window(self):
        self.showMinimized()

    def client_image(self, qimage):
        self.save_image(qimage)
        file_path = './GUI/icons/ava.jpg'
        imgdata = open(file_path, 'rb').read()
        imgtype = file_path[-3:]
        pixmap = self.mask_image(imgdata, imgtype)
        self.ui.icon_user.setStyleSheet('')
        self.ui.icon_user.setPixmap(pixmap)

    def save_image(self, qimage):
        with open(f'./GUI/icons/ava.jpg', 'wb') as received_image_file:
            received_image_file.write(qimage)

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
            self.original_items = [self.ui.list_users.item(i).text() for i in range(self.ui.list_users.count())]

    @Slot(str)
    def user_add_db(self, users):
        users = users.split(', ')
        for user in users:
            self.ui.list_users.addItem(user)
        self.original_items = [self.ui.list_users.item(i).text() for i in range(self.ui.list_users.count())]

    @Slot(str)
    def add_messages(self, messages):
        messages = messages[1:-1]
        result = re.findall(r'\((.*?)\)', messages)
        ite = [item.replace("'", "") for item in result]
        ite = [item.split(', ') for item in ite]
        messages = ''
        for itt in ite:
            print_time = itt[3].split(' ')
            print_data = print_time[1]
            print_time = print_time[1][:5]
            if itt[0] != Constant().login:
                direct = 'left'
            else:
                direct = 'right'
            messages += (
                f"\n<div style='text-align:{direct};'>"
                f"<span style='display: inline-block; border: 2px solid red; border-radius: 50%; padding: 5px;'>"
                f"<span style='font-size: larger;'>{itt[2]}</span>"
                f"</span>"
                f" "
                f"<span style='display: inline-block; border: 2px solid blue; border-radius: 50%; padding: 5px;'>"
                f"<span style='font-size: 8pt;'>{print_time}</span>"
                f"</span>"
                f"</div>"
            )

        self.ui.sms_label.setText(messages)


    def send_message(self):
            msg = str(self.ui.send_text.toPlainText())
            try:
                user_send = self.ui.list_users.currentItem().text()
            except:
                return
            if msg == '' or user_send == '':
                return
            else:
                message = f'user: {Constant().login} ' + 'to: ' + user_send + ' #!msg: ' + msg
                self.signal_send_message.emit(message)
                print_time = str(datetime.datetime.now())[11:16]
                msg = (
                f"\n<div style='text-align:right;'>"
                f"<span style='display: inline-block; border: 2px solid red; border-radius: 50%; padding: 5px;'>"
                f"<span style='font-size: larger;'>{msg}</span>"
                f"</span>"
                f" "
                f"<span style='display: inline-block; border: 2px solid blue; border-radius: 50%; padding: 5px;'>"
                f"<span style='font-size: 8pt;'>{print_time}</span>"
                f"</span>"
                f"</div>"
            )
                messages = self.ui.sms_label.text()
                messages += msg
                self.ui.sms_label.setText(messages)
                self.ui.send_text.clear()
                self.ui.send_text.update()
                self.ui.send_text.setAcceptRichText(False)

    def scrollToBottom(self, minVal=None, maxVal=None):
        self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())

    def eventFilter(self, obj, event):
        if (event.type() == QEvent.KeyPress):
            key = event.key()
            if key == Qt.Key_Escape:
                if self.ui.menu_bar_settings.width() != 0:
                    self.ui.menu_bar_settings.collapseMenu()
                    self.blur_effect.setEnabled(False)
                else:
                    self.ui.stackedWidget_sms.setCurrentIndex(1)
                    self.ui.user_label.clear()
                    self.ui.list_users.clearSelection()
        if obj is self.ui.send_text and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return and not event.modifiers():
                self.send_message()
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                return True
        return super().eventFilter(obj, event)

    def user_choise(self):
        msg = 'select: ' + 'user: ' + Constant().login + ' user_send: ' + self.ui.list_users.currentItem().text()
        self.signal_send_message.emit(msg)

    @Slot(str)
    def show_activ_user(self, activ):
        time = str(datetime.datetime.now())
        if int(activ[2:3]) == 0:
            if time[:11] == activ[6:17]:
                if int(time[14:16]) - int(activ[20:22]) > 30:
                    status = 'Был в сети ' + str(int(int(activ[20:22]) - int(time[14:16]))) + ' минут назад'
                else:
                    status = 'Был в сети ' + activ[17:22]
            else:
                day = activ[14:16]
                month = activ[11:13]
                status = 'Был(а) ' + day + "." + month + "." + activ[6:10] + ' в ' + activ[17:22]
        elif int(activ[2:3]) == 1:
            status = 'В сети'
        else:
            status = 'Error'

        self.ui.stackedWidget_sms.setCurrentIndex(0)
        self.shoise_user = self.ui.list_users.currentItem().text()
        self.ui.user_label.setText(self.shoise_user)
        self.ui.user_status.setText(status)

    def put_text_search(self):
        self.ui.search_text.clear()

    def effects(self):
        self.blur_effect.setEnabled(True)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.ui.icon_user.geometry().contains(event.pos()):
            self.load_icon()
        if event.button() == Qt.LeftButton and self.ui.widget_btn.geometry().contains(event.pos()):
            self.oldPosition = event.pos()
        if event.button() == Qt.LeftButton and self.ui.widget_right_main.geometry().contains(event.pos()):
            if self.ui.menu_bar_settings.width() != 0:
                self.ui.menu_bar_settings.collapseMenu()
                self.blur_effect.setEnabled(False)
        if event.button() == Qt.LeftButton and self.ui.wd_close.geometry().contains(event.pos()):
            # self.user_exit()
            print('exit_user')
        return super().mousePressEvent(event)


    def mouseMoveEvent(self, event):
        try:
            if self.oldPosition is not None:
                delta = QPoint(event.pos() - self.oldPosition)
                self.move(self.x() + delta.x(), self.y() + delta.y())
        except:
            return

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPosition = None


    def menu_bar_settings(self):
        self.ui.name_user.setText(Constant().login)


    def user_exit(self):
        paragraph = 'Authentication parameters'
        Constant().shanges(paragraph, 'AUTHORIZED', 'False')
        Constant().shanges(paragraph, 'login', '')
        Constant().shanges(paragraph, 'password', '')

        message = '#!info ' + '!DISCONNECT ' + Constant().login
        self.signal_send_message.emit(message)
        self.close()

    def load_icon(self):
        if self.ui.menu_bar_settings.width() == 0:
            return
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.jpg)")
        if file_path:
            imgdata = open(file_path, 'rb').read()
            imgtype = file_path[-3:]
            if imgtype == 'png':
                return
            pixmap = self.mask_image(imgdata, imgtype)
            self.ui.icon_user.setStyleSheet('')
            self.ui.icon_user.setPixmap(pixmap)
            self.sender.send_ico(file_path)

    def mask_image(self, imgdata, imgtype='jpg', size=64):

        image = QImage.fromData(imgdata, imgtype)
        image.convertToFormat(QImage.Format_ARGB32)

        imgsize = int(min(image.width(), image.height()))
        rect = QRect(int((image.width() - imgsize) / 2), int((image.height() - imgsize) / 2), imgsize, imgsize)
        image = image.copy(rect)

        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)

        brush = QBrush(image)
        painter = QPainter(out_img)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawEllipse(0, 0, imgsize, imgsize)
        painter.end()

        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        pm = pm.scaled(self.ui.icon_user.width(), self.ui.icon_user.height(), Qt.KeepAspectRatio)
        return pm

