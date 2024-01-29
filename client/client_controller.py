import sys
import datetime

from PyQt5.QtGui import QPixmap, QImage, QBrush, QPainter, QWindow
from Custom_Widgets import loadJsonStyle
from GUI.UI_MainWindow import Ui_MainWindow
from Custom.CustomQListWidget import CustomQListWidgetItem
from authorization import Authorization
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QGraphicsBlurEffect, QListWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal as Signal, pyqtSlot as Slot, QPoint, QEvent, QRect, QSize
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
        self.width_size = None
        self.height_size = None
        self.original_items = []
        self.ui.widget_send_text.hide()
        self.ui.list_users.setSpacing(0)

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
        pass
        # if self.ui.list_users.count() == 0:
        #     return
        # if self.ui.search_text.toPlainText() == '':
        #     for i in range(self.ui.list_users.count()):
        #         self.ui.list_users.takeItem(0)
        #     for i in range(len(self.original_items)):
        #         self.ui.list_users.addItem(self.original_items[i])
        #
        # search_text = self.ui.search_text.toPlainText().lower()
        # item_anywhere = self.ui.list_users.findItems(search_text, Qt.MatchContains)
        #
        # start_list = list(filter(lambda item: item.text().lower().startswith(search_text), item_anywhere))
        # start_text = [x.text().lower() for x in start_list]
        #
        # def bw_filter(item):
        #     item_text = item.text().lower()
        #     return search_text in item_text[1:-1] and item_text not in start_text
        #
        # bw_lst = list(filter(bw_filter, item_anywhere))
        # bw_lst.sort(key=lambda item: item.text().lower().find(search_text))
        # bw_text = [x.text().lower() for x in bw_lst]
        #
        # def end_filter(item):
        #     item_text = item.text().lower()
        #     return item_text.endswith(search_text) and item_text.lower() not in start_text and item_text not in bw_text
        #
        # end_lst = list(filter(end_filter, item_anywhere))
        # end_lst.sort(key=lambda item: item.text().lower().find(search_text))
        #
        #
        # for i in range(self.ui.list_users.count()):
        #     self.ui.list_users.takeItem(0)
        #
        # for item in start_list + bw_lst + end_lst:
        #     self.ui.list_users.addItem(item.text())
        #
        # for i in range(len(self.original_items)):
        #     item_text = self.original_items[i]
        #     existing_items = self.ui.list_users.findItems(item_text, Qt.MatchExactly)
        #     if not existing_items:
        #         self.ui.list_users.addItem(item_text)
        #     else:
        #         pass

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
        self.ui.list_users.itemClicked.connect(self.user_choise)
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
        self.sender.signal_notiff.connect(self.notification)
        self.sender.signal_activ.connect(self.show_activ_user)

        self.sender.signal_image.connect(self.client_image)

        self.ui.send_text.installEventFilter(self)
        self.installEventFilter(self)
        self.ui.list_users.installEventFilter(self)

        self.ui.btn_settings.clicked.connect(self.effects)

    def init_const(self):
        self.shoise_user = None
        self.notif_count = {}
        self.ui.send_text.setAcceptRichText(False)
        self.ui.stackedWidget_sms.setCurrentIndex(1)
        self.menu_bar_settings()
        loadJsonStyle(self, self.ui, jsonFiles={"GUI\style.json"})
        self.blur_effect = QGraphicsBlurEffect()
        self.ui.widget_right_main.setGraphicsEffect(self.blur_effect)
        self.blur_effect.setEnabled(False)
        self.ui.app_text.setText(
            '<a href="https://github.com/Vityshha/desktop-messenger/tree/main" style="color: white; text-decoration: none;">KFU Desktop Messaging</a>')

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
        # todo нужно ждать вдруг не успело
        with open(f'./cache/images/ava.jpg', 'wb') as received_image_file:
            received_image_file.write(qimage)

        file_path = './cache/images/ava.jpg'
        imgdata = open(file_path, 'rb').read()
        imgtype = file_path[-3:]
        pixmap = self.mask_image(imgdata, imgtype)
        self.ui.icon_user.setStyleSheet('')
        self.ui.icon_user.setPixmap(pixmap)

    @Slot(str)
    def user_add(self, user):
        '''Поиск и добавление пользователей если они есть в бд
                    и если они еще не добавлены'''
        self.books = []
        for i in range(self.ui.list_users.count()):
            book = self.ui.list_users.item(i).data(Qt.UserRole)['login']
            self.books.append(book)
        if user in self.books:
            return
        else:
            if user not in self.original_items:
                self.original_items.append(user)
                self.add_search_user(user)

    def compare_dates(self, item):
        return datetime.datetime.strptime(item[1], '%Y-%m-%d %H:%M')

    @Slot(str)
    def user_add_db(self, users):
        # todo добавить непрочитанные смс
        matches = re.findall(r"\('([^']+)', '(\d{4}-\d{2}-\d{2} \d{2}:\d{2}):\d{2}\.\d{6}', '([^']+)'\)", users)
        result = [(match[0], match[1], match[2]) for match in matches]
        sorted_data = sorted(result, key=self.compare_dates, reverse=True)
        for user in sorted_data:
            login = user[0]
            self.notif_count[login] = 0
            time = user[1][11:]
            last_sms = user[2]
            if user not in self.original_items:
                self.original_items.append(login)
                self.add_item({"login": login,
                               'avatar': 'C:\\Users\\KFU\\Desktop\\desktop-messenger\\client\\GUI\\icons\\ava.jpg',
                               'last_sms': last_sms, 'time_sms': time, 'notif_count': ''})

    def add_item(self, user_data):
        item = QListWidgetItem()
        item.setData(Qt.UserRole, user_data)
        item.setSizeHint(QSize(self.ui.widget_users_list.width() - 30, 80))
        widget = CustomQListWidgetItem(data=user_data)
        self.ui.list_users.addItem(item)
        self.ui.list_users.setItemWidget(item, widget)

    def add_search_user(self, users):
        matches = re.findall(r"\('([^']+)', '(\d{4}-\d{2}-\d{2} \d{2}:\d{2}):\d{2}\.\d{6}'\)", users)
        result = [(match[0], match[1]) for match in matches]
        sorted_data = sorted(result, key=self.compare_dates, reverse=True)
        for user in sorted_data:
            login = user[0]
            time = user[1][11:]
            if user not in self.original_items:
                self.original_items.append(login)
                self.add_item({"login": login,
                               'avatar': 'C:\\Users\\KFU\\Desktop\\desktop-messenger\\client\\GUI\\icons\\ava.jpg',
                               'last_sms': '', 'time_sms': '', 'notif_count': ''})

    @Slot(str)
    def add_messages(self, messages):
        messages = messages[1:-1]
        result = re.findall(r'\((.*?)\)', messages)
        ite = [item.replace("'", "") for item in result]
        ite = [item.split(', ') for item in ite]
        messages = ''
        for itt in ite:
            user = itt[0]
            print_time = itt[3].split(' ')
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

    @Slot(str)
    def notification(self, notif):
        #todo можно оптимизировать
        messages = notif[1:-1]
        result = re.findall(r'\((.*?)\)', messages)
        ite = [item.replace("'", "") for item in result]
        ite = [item.split(', ') for item in ite]
        user = ite[0][0]
        messages = self.ui.sms_label.text()
        current_user = self.ui.list_users.currentItem()
        for itt in ite:
            print_time = itt[3].split(' ')
            print_time = print_time[1][:5]
            if itt[0] != Constant().login:
                direct = 'left'
                if current_user:
                    if current_user.data(Qt.UserRole)['login'] != user:
                        if f'{itt[0]}' in self.notif_count:
                            self.notif_count[f'{itt[0]}'] += 1
                        else:
                            self.notif_count[f'{itt[0]}'] = 1
                else:
                    if f'{itt[0]}' in self.notif_count:
                        self.notif_count[f'{itt[0]}'] += 1
                    else:
                        self.notif_count[f'{itt[0]}'] = 1
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

        self.move_item_to_top(notif=True, user=user, msg=ite[0][2], time=ite[0][3][11:16])
        if current_user:
            if user == self.ui.list_users.currentItem().data(Qt.UserRole)['login']:
                self.ui.sms_label.setText(messages)

    def move_item_to_top(self, notif=None, user=None, msg=None, time=None):
        if notif:
            if user not in self.original_items:
                self.original_items.append(user)
                self.notif_count[user] = 1
                self.add_item(
                    {"login": user, 'avatar': 'C:\\Users\\KFU\\Desktop\\desktop-messenger\\client\\GUI\\icons\\ava.jpg',
                     'last_sms': msg, 'time_sms': time, 'notif_count': self.notif_count[user]})
            current_item = self.ui.list_users.currentItem()
            for i in range(self.ui.list_users.count()):
                if self.ui.list_users.item(i).data(Qt.UserRole)['login'] == user:
                    row = i
                    items_info = self.ui.list_users.item(i).data(Qt.UserRole)
                    items_info['last_sms'] = msg
                    items_info['time_sms'] = str(datetime.datetime.now())[11:16]
                    items_info['notif_count'] = str(self.notif_count[user])

                    new_item = QListWidgetItem()
                    new_item.setData(Qt.UserRole, items_info)
                    new_item.setSizeHint(QSize(self.ui.widget_users_list.width() - 30, 80))
                    new_widget = CustomQListWidgetItem(data=items_info)

                    self.ui.list_users.takeItem(row)
                    self.ui.list_users.insertItem(0, new_item)
                    self.ui.list_users.setItemWidget(new_item, new_widget)
                    if current_item:
                        row = self.ui.list_users.row(current_item)
                        if row == None:
                            break
                        elif row == -1:
                            row = 0
                            self.ui.list_users.setCurrentRow(row)
                    break
        else:
            current_item = self.ui.list_users.currentItem()
            items_info = current_item.data(Qt.UserRole)
            if items_info:
                items_info['last_sms'] = msg
                items_info['time_sms'] = str(datetime.datetime.now())[11:16]
                items_info['notif_count'] = ''
                self.notif_count[str(items_info['login'])] = 0

                new_item = QListWidgetItem()
                new_item.setData(Qt.UserRole, items_info)
                new_item.setSizeHint(QSize(self.ui.widget_users_list.width() - 30, 80))
                new_widget = CustomQListWidgetItem(data=items_info)

                row = self.ui.list_users.row(current_item)
                self.ui.list_users.takeItem(row)
                self.ui.list_users.insertItem(0, new_item)
                self.ui.list_users.setItemWidget(new_item, new_widget)
                self.ui.list_users.setCurrentRow(0)

    def send_message(self):
        msg = str(self.ui.send_text.toPlainText())
        try:
            user_send = self.ui.user_label.text()
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
            if Constant().login == self.ui.user_label.text():
                pass
            else:
                self.ui.sms_label.setText(messages)

            self.move_item_to_top(notif=False, user=user_send, msg=str(self.ui.send_text.toPlainText()))

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
                    self.ui.user_status.clear()
                    self.ui.widget_send_text.hide()
                    self.ui.list_users.clearFocus()
                    self.ui.list_users.clearSelection()
                    self.ui.list_users.setCurrentItem(None)
        if obj is self.ui.send_text and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return and not event.modifiers():
                self.send_message()
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                return True
        return super().eventFilter(obj, event)

    def user_choise(self):
        self.ui.widget_send_text.show()
        user_select = self.ui.list_users.currentItem().data(Qt.UserRole)['login']
        msg = 'select: ' + 'user: ' + Constant().login + ' user_send: ' + user_select
        self.signal_send_message.emit(msg)

        current_item = self.ui.list_users.currentItem()
        items_info = current_item.data(Qt.UserRole)
        if items_info and (items_info['notif_count'] != 0 or items_info['notif_count'] != ''):
            items_info['notif_count'] = ''
            self.notif_count[str(user_select)] = 0

            new_item = QListWidgetItem()
            new_item.setData(Qt.UserRole, items_info)
            new_item.setSizeHint(QSize(self.ui.widget_users_list.width() - 30, 80))
            new_widget = CustomQListWidgetItem(data=items_info)

            row = self.ui.list_users.row(current_item)
            self.ui.list_users.takeItem(row)
            self.ui.list_users.insertItem(row, new_item)
            self.ui.list_users.setItemWidget(new_item, new_widget)
            self.ui.list_users.setCurrentRow(row)

    @Slot(str)
    def show_activ_user(self, activ):
        time = str(datetime.datetime.now())

        if activ == [] or activ == '[]':
            return

        if int(activ[2:3]) == 0:
            if time[:11] == activ[6:17]:
                status = 'Был(а) в сети ' + activ[17:22]
            else:
                day = activ[14:16]
                month = activ[11:13]
                status = 'Был(а) ' + day + "." + month + "." + activ[6:10] + ' в ' + activ[17:22]
        elif int(activ[2:3]) == 1:
            status = 'В сети'
        else:
            status = 'Error'

        self.ui.stackedWidget_sms.setCurrentIndex(0)
        self.shoise_user = self.ui.list_users.currentItem().data(Qt.UserRole)['login']
        self.ui.user_label.setText(self.shoise_user)
        self.ui.user_status.setText(status)

    def put_text_search(self):
        self.ui.search_text.clear()

    def effects(self):
        self.blur_effect.setEnabled(True)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton and not self.ui.widget_btn.geometry().contains(event.pos()):
            if event.x() >= self.width() - 5:
                self.width_size = event.globalPos()
                event.accept()
                self.setCursor(Qt.SizeHorCursor)
            elif event.y() >= self.height() - 5:
                self.height_size = event.globalPos()
                event.accept()
                self.setCursor(Qt.SizeVerCursor)
            else:
                pass

        if event.button() == Qt.LeftButton and self.ui.icon_user.geometry().contains(event.pos()):
            self.load_icon()
        if event.button() == Qt.LeftButton and self.ui.widget_btn.geometry().contains(event.pos()):
            self.oldPosition = event.pos()
        if event.button() == Qt.LeftButton and self.ui.widget_right_main.geometry().contains(event.pos()):
            if self.ui.menu_bar_settings.width() != 0:
                self.ui.menu_bar_settings.collapseMenu()
                self.blur_effect.setEnabled(False)

        if event.button() == Qt.LeftButton:
            wd_close_global_pos = self.ui.wd_close.mapToGlobal(QPoint(0, 0))
            if wd_close_global_pos.x() <= event.globalX() <= wd_close_global_pos.x() + self.ui.wd_close.width() and \
                    wd_close_global_pos.y() <= event.globalY() <= wd_close_global_pos.y() + self.ui.wd_close.height():
                self.user_exit()
        return super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton and self.ui.widget_btn.geometry().contains(event.pos()):
            self.resize_window()
        return super().mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event):

        if self.width_size is not None:
            delta = event.globalPos() - self.width_size
            self.resize(self.width() + delta.x(), self.height())
            self.width_size = event.globalPos()
            event.accept()

        if self.height_size is not None:
            delta = event.globalPos() - self.height_size
            self.resize(self.width(), self.height() + delta.y())
            self.height_size = event.globalPos()
            event.accept()

        try:
            if self.oldPosition is not None:
                delta = QPoint(event.pos() - self.oldPosition)
                self.move(self.x() + delta.x(), self.y() + delta.y())
        except:
            return

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPosition = None
            self.setCursor(Qt.ArrowCursor)
            self.width_size = None
            self.height_size = None
            event.accept()

    def menu_bar_settings(self):
        self.ui.name_user.setText(Constant().login)

    def user_exit(self):
        message = '#!info ' + '!RESTART ' + Constant().login
        self.signal_send_message.emit(message)
        paragraph = 'Authentication parameters'
        Constant().shanges(paragraph, 'AUTHORIZED', 'False')
        Constant().shanges(paragraph, 'login', '')
        Constant().shanges(paragraph, 'password', '')

        # restart app
        self.ui.list_users.clear()
        self.ui.icon_user.clear()
        self.ui.sms_label.clear()
        self.ui.user_status.clear()
        self.ui.user_label.clear()
        self.ui.stackedWidget_sms.setCurrentIndex(1)
        self.Authorization.ui_authorization.password.clear()
        self.Authorization.ui_authorization.login.clear()
        self.Authorization.ui_authorization.login.setFocus()
        self.ui.menu_bar_settings.collapseMenu()
        self.blur_effect.setEnabled(False)
        self.hide()
        self.login_messager()

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
