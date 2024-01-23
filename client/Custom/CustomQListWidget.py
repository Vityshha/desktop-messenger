from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtGui import QPixmap, QImage, QBrush, QPainter, QWindow, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QListWidgetItem, QListWidget, QSpacerItem, \
    QSizePolicy


class CustomQListWidget:

    def __init__(self, wight=200):
        super(CustomQListWidget, self).__init__()
        self.width_size = wight

    def get_item_widget(self, data):
        # Read attributes
        login = data['login']
        avatar = data['avatar']
        last_sms = data['last_sms']
        time_sms = data['time_sms']
        # Total Widget
        wight = QWidget()

        login_label = QLabel(login)
        login_label.setFont(QFont("Open Sans", 10, QFont.Bold))

        last_sms_label = QLabel(last_sms)
        last_sms_label.setFont(QFont("Open Sans", 10))
        last_sms_label.setStyleSheet("color: gray;")

        time_sms_label = QLabel(time_sms)
        time_sms_label.setFont(QFont("Open Sans", 8))
        time_sms_label.setStyleSheet("color: gray;")

        # Overall horizontal layout
        layout_main = QHBoxLayout()
        layout_main.setSpacing(8)
        layout_main.setContentsMargins(0, 0, 0, 0)
        self.map_l = QLabel()  # Avatar display
        self.map_l.setFixedSize(40, 40)
        maps = QPixmap(avatar)
        pixmap = self.mask_image(maps)

        self.map_l.setPixmap(pixmap)

        # Vertical layout on the right
        layout_right = QVBoxLayout()

        # Horizontal layout of the bottom right
        layout_right_down = QHBoxLayout()  # Horizontal layout at the bottom right
        layout_right_down.addWidget(last_sms_label)


        # Horizontal layout for login_label and time_sms_label
        layout_login_time = QHBoxLayout()
        layout_login_time.addWidget(login_label)
        layout_login_time.addSpacerItem(QSpacerItem(125, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))
        layout_login_time.addWidget(time_sms_label)

        # Follow the layout from left to right, top to bottom to add
        layout_main.addWidget(self.map_l)  # The leftmost picture

        layout_right.addLayout(layout_login_time)  # Add layout_login_time instead of login_label
        layout_right.addLayout(layout_right_down)  # Horizontal layout in the lower right corner

        layout_main.addLayout(layout_right)  # Layout on the right

        wight.setLayout(layout_main)  # Layout for wight
        return wight

    def mask_image(self, imgdata, imgtype='jpg', size=45):
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

        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        pm = pm.scaled(self.map_l.width(), self.map_l.height(), Qt.KeepAspectRatio)
        return pm