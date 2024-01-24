from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtGui import QPixmap, QImage, QBrush, QPainter, QWindow, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QListWidgetItem, QListWidget, QSpacerItem, \
    QSizePolicy


class CustomQListWidgetItem(QWidget):
    def __init__(self, data, parent=None):
        super(CustomQListWidgetItem, self).__init__(parent)
        self.width_size = 200
        self.setStyleSheet('background: transparent;')
        self.init_ui(data)


    def init_ui(self, data):
        login = data['login']
        avatar = data['avatar']
        last_sms = data['last_sms']
        time_sms = data['time_sms']

        login_label = QLabel(login)
        login_label.setFont(QFont("Open Sans", 9, QFont.Bold))

        last_sms_label = QLabel(last_sms)
        last_sms_label.setFont(QFont("Open Sans", 10))
        last_sms_label.setStyleSheet("color: gray;")

        time_sms_label = QLabel(time_sms)
        time_sms_label.setFont(QFont("Open Sans", 8))
        time_sms_label.setStyleSheet("color: gray;")

        map_label = QLabel()
        map_label.setFixedSize(60, 60)
        maps = QPixmap(avatar)
        pixmap = self.mask_image(maps)

        map_label.setPixmap(pixmap)

        layout_main = QHBoxLayout()
        layout_main.setSpacing(8)
        layout_main.setContentsMargins(10, 0, 10, 0)

        layout_right = QVBoxLayout()

        layout_right_down = QHBoxLayout()  # Горизонтальный макет в правом нижнем углу
        layout_right_down.addWidget(last_sms_label)
        layout_right_down.setContentsMargins(8, 0, 0, 12)

        layout_login_time = QHBoxLayout()
        layout_login_time.addWidget(login_label)
        layout_login_time.addSpacerItem(QSpacerItem(self.width_size, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        layout_login_time.addWidget(time_sms_label)
        layout_login_time.setContentsMargins(8, 12, 0, 0)

        layout_main.addWidget(map_label)  # Левое изображение

        layout_right.addLayout(layout_login_time)
        layout_right.addLayout(layout_right_down)

        layout_main.addLayout(layout_right)

        self.setLayout(layout_main)

    def mask_image(self, imgdata, imgtype='jpg', size=60):
        if isinstance(imgdata, QPixmap):
            image = imgdata.toImage()
        else:
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

        pr = self.devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        pm = pm.scaled(size, size, Qt.KeepAspectRatio)
        return pm