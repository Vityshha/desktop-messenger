# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(70, 64, 98);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_btn = QtWidgets.QWidget(self.widget)
        self.widget_btn.setObjectName("widget_btn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_btn)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_remove = QtWidgets.QPushButton(self.widget_btn)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_remove.setFont(font)
        self.btn_remove.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_remove.setMouseTracking(True)
        self.btn_remove.setTabletTracking(True)
        self.btn_remove.setStyleSheet("QPushButton {\n"
"    border: 0px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 0px;\n"
"    image: url(GUI/icons/remove.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(90, 80, 120);\n"
"}")
        self.btn_remove.setText("")
        self.btn_remove.setObjectName("btn_remove")
        self.horizontalLayout.addWidget(self.btn_remove)
        self.btn_shape = QtWidgets.QPushButton(self.widget_btn)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_shape.setFont(font)
        self.btn_shape.setStyleSheet("QPushButton {\n"
"    border: 0px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 0px;\n"
"    image: url(GUI/icons/check_box.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(90, 80, 120);\n"
"}")
        self.btn_shape.setText("")
        self.btn_shape.setObjectName("btn_shape")
        self.horizontalLayout.addWidget(self.btn_shape)
        self.btn_close = QtWidgets.QPushButton(self.widget_btn)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: 0px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 0px;\n"
"    image: url(GUI/icons/close.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout_2.addWidget(self.widget_btn, 0, QtCore.Qt.AlignTop)
        self.widget_main = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy)
        self.widget_main.setObjectName("widget_main")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_main)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_bar_settings = QCustomSlideMenu(self.widget_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_bar_settings.sizePolicy().hasHeightForWidth())
        self.menu_bar_settings.setSizePolicy(sizePolicy)
        self.menu_bar_settings.setStyleSheet("background-color: rgb(54, 50, 87);")
        self.menu_bar_settings.setObjectName("menu_bar_settings")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.menu_bar_settings)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.user_info = QtWidgets.QWidget(self.menu_bar_settings)
        self.user_info.setObjectName("user_info")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.user_info)
        self.verticalLayout_10.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.icon_user = QtWidgets.QLabel(self.user_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_user.sizePolicy().hasHeightForWidth())
        self.icon_user.setSizePolicy(sizePolicy)
        self.icon_user.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(40)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.icon_user.setFont(font)
        self.icon_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_user.setStyleSheet("image: url(GUI/icons/person.png);\n"
"border: 3px;\n"
"border-radius: 40px;")
        self.icon_user.setText("")
        self.icon_user.setObjectName("icon_user")
        self.verticalLayout_10.addWidget(self.icon_user, 0, QtCore.Qt.AlignLeft)
        self.line_3 = QtWidgets.QFrame(self.user_info)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        self.name_user = QtWidgets.QLabel(self.user_info)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_user.setFont(font)
        self.name_user.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_user.setObjectName("name_user")
        self.verticalLayout_10.addWidget(self.name_user, 0, QtCore.Qt.AlignBottom)
        self.line = QtWidgets.QFrame(self.user_info)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_10.addWidget(self.line)
        self.verticalLayout_9.addWidget(self.user_info, 0, QtCore.Qt.AlignTop)
        self.more_settings = QtWidgets.QWidget(self.menu_bar_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.more_settings.sizePolicy().hasHeightForWidth())
        self.more_settings.setSizePolicy(sizePolicy)
        self.more_settings.setObjectName("more_settings")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.more_settings)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.wd_create_group = QtWidgets.QWidget(self.more_settings)
        self.wd_create_group.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wd_create_group.setMouseTracking(True)
        self.wd_create_group.setStyleSheet("QWidget:hover  {\n"
"    background: rgb(70, 65, 100);\n"
"}\n"
"\n"
"")
        self.wd_create_group.setObjectName("wd_create_group")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.wd_create_group)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.wd_create_group)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setStyleSheet("image: url(GUI/icons/group.png);\n"
"border : 0;\n"
"background: transparent;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.label_12 = QtWidgets.QLabel(self.wd_create_group)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(" border : 0;\n"
"    background: transparent;\n"
"    color: rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_12.addWidget(self.wd_create_group)
        self.wd_account = QtWidgets.QWidget(self.more_settings)
        self.wd_account.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wd_account.setMouseTracking(True)
        self.wd_account.setStyleSheet("QWidget:hover{\n"
"    background: rgb(70, 65, 100);\n"
"}")
        self.wd_account.setObjectName("wd_account")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.wd_account)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.wd_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setStyleSheet("image: url(GUI/icons/account.png);\n"
"border : 0;\n"
"background: transparent;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.label_11 = QtWidgets.QLabel(self.wd_account)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(" border : 0;\n"
"    background: transparent;\n"
"    color: rgb(255, 255, 255)")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_12.addWidget(self.wd_account)
        self.wd_call = QtWidgets.QWidget(self.more_settings)
        self.wd_call.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wd_call.setMouseTracking(True)
        self.wd_call.setStyleSheet("QWidget:hover{\n"
"    background: rgb(70, 65, 100);\n"
"}")
        self.wd_call.setObjectName("wd_call")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.wd_call)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.wd_call)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setStyleSheet("image: url(GUI/icons/call.png);\n"
"border : 0;\n"
"background: transparent;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(self.wd_call)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(" border : 0;\n"
"    background: transparent;\n"
"    color: rgb(255, 255, 255)")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_12.addWidget(self.wd_call)
        self.wd_settings = QtWidgets.QWidget(self.more_settings)
        self.wd_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wd_settings.setMouseTracking(True)
        self.wd_settings.setStyleSheet("QWidget:hover{\n"
"    background: rgb(70, 65, 100);\n"
"}")
        self.wd_settings.setObjectName("wd_settings")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.wd_settings)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.wd_settings)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setStyleSheet("image: url(GUI/icons/settings.png);\n"
"border : 0;\n"
"background: transparent;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.wd_settings)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(" border : 0;\n"
"    background: transparent;\n"
"    color: rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayout_12.addWidget(self.wd_settings)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        self.wd_close = QtWidgets.QWidget(self.more_settings)
        self.wd_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wd_close.setMouseTracking(True)
        self.wd_close.setStyleSheet("QWidget:hover{\n"
"    background: rgb(70, 65, 100);\n"
"}")
        self.wd_close.setObjectName("wd_close")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.wd_close)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.wd_close)
        self.label_6.setMinimumSize(QtCore.QSize(50, 0))
        self.label_6.setStyleSheet("image: url(GUI/icons/logout.png);\n"
"border : 0;\n"
"background: transparent;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.wd_close)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(" border : 0;\n"
"    background: transparent;\n"
"    color: rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_12.addWidget(self.wd_close)
        self.verticalLayout_9.addWidget(self.more_settings)
        self.app_info = QtWidgets.QWidget(self.menu_bar_settings)
        self.app_info.setObjectName("app_info")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.app_info)
        self.verticalLayout_11.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.line_2 = QtWidgets.QFrame(self.app_info)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_11.addWidget(self.line_2)
        self.app_text = QtWidgets.QLabel(self.app_info)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.app_text.setFont(font)
        self.app_text.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.app_text.setOpenExternalLinks(True)
        self.app_text.setObjectName("app_text")
        self.verticalLayout_11.addWidget(self.app_text)
        self.app_text_2 = QtWidgets.QLabel(self.app_info)
        self.app_text_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.app_text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.app_text_2.setOpenExternalLinks(True)
        self.app_text_2.setObjectName("app_text_2")
        self.verticalLayout_11.addWidget(self.app_text_2)
        self.verticalLayout_9.addWidget(self.app_info)
        self.horizontalLayout_2.addWidget(self.menu_bar_settings)
        self.widget_left_main = QtWidgets.QWidget(self.widget_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left_main.sizePolicy().hasHeightForWidth())
        self.widget_left_main.setSizePolicy(sizePolicy)
        self.widget_left_main.setStyleSheet("background-color: rgb(54, 50, 87);")
        self.widget_left_main.setObjectName("widget_left_main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_left_main)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_settings = QtWidgets.QWidget(self.widget_left_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_settings.sizePolicy().hasHeightForWidth())
        self.widget_settings.setSizePolicy(sizePolicy)
        self.widget_settings.setObjectName("widget_settings")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_settings)
        self.horizontalLayout_3.setContentsMargins(0, 6, 10, 6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_settings = QtWidgets.QPushButton(self.widget_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_settings.setFont(font)
        self.btn_settings.setStyleSheet("QPushButton {\n"
"    border: 0px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 0px;\n"
"    image: url(GUI/icons/menu.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(70, 65, 100);\n"
"}")
        self.btn_settings.setText("")
        self.btn_settings.setIconSize(QtCore.QSize(16, 16))
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout_3.addWidget(self.btn_settings, 0, QtCore.Qt.AlignLeft)
        self.search_text = QtWidgets.QTextEdit(self.widget_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_text.sizePolicy().hasHeightForWidth())
        self.search_text.setSizePolicy(sizePolicy)
        self.search_text.setMaximumSize(QtCore.QSize(200, 16777215))
        self.search_text.setAcceptDrops(False)
        self.search_text.setStyleSheet("background-color: rgb(70, 64, 98);\n"
"color: rgba(255, 255, 255,1);\n"
"border: 2px solid rgba(62, 63, 70, 0);\n"
"border-radius: 12px;")
        self.search_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.search_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.search_text.setTabChangesFocus(True)
        self.search_text.setOverwriteMode(False)
        self.search_text.setAcceptRichText(True)
        self.search_text.setObjectName("search_text")
        self.horizontalLayout_3.addWidget(self.search_text)
        self.verticalLayout_3.addWidget(self.widget_settings)
        self.widget_users_list = QtWidgets.QWidget(self.widget_left_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_users_list.sizePolicy().hasHeightForWidth())
        self.widget_users_list.setSizePolicy(sizePolicy)
        self.widget_users_list.setStyleSheet("QListWidget::item:selected\n"
"{\n"
"    background: rgb(64, 57, 101);\n"
"    border: transparent;\n"
"}\n"
"\n"
"QListWidget::item:hover\n"
"{\n"
"    background: rgb(64, 57, 101);\n"
"    border: transparent;\n"
"}")
        self.widget_users_list.setObjectName("widget_users_list")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_users_list)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.list_users = QtWidgets.QListWidget(self.widget_users_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_users.sizePolicy().hasHeightForWidth())
        self.list_users.setSizePolicy(sizePolicy)
        self.list_users.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: transparent;\n"
"outline: 0;\n"
"")
        self.list_users.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_users.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_users.setObjectName("list_users")
        self.verticalLayout_7.addWidget(self.list_users)
        self.verticalLayout_3.addWidget(self.widget_users_list)
        self.horizontalLayout_2.addWidget(self.widget_left_main, 0, QtCore.Qt.AlignLeft)
        self.widget_right_main = QtWidgets.QWidget(self.widget_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_right_main.sizePolicy().hasHeightForWidth())
        self.widget_right_main.setSizePolicy(sizePolicy)
        self.widget_right_main.setObjectName("widget_right_main")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_right_main)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_user = QtWidgets.QWidget(self.widget_right_main)
        self.widget_user.setStyleSheet("background-color: rgb(54, 50, 87);")
        self.widget_user.setObjectName("widget_user")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_user)
        self.verticalLayout_5.setContentsMargins(-1, 5, 0, 5)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.user_label = QtWidgets.QLabel(self.widget_user)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_label.sizePolicy().hasHeightForWidth())
        self.user_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.user_label.setFont(font)
        self.user_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_label.setText("")
        self.user_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_label.setObjectName("user_label")
        self.verticalLayout_5.addWidget(self.user_label)
        self.user_status = QtWidgets.QLabel(self.widget_user)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_status.sizePolicy().hasHeightForWidth())
        self.user_status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.user_status.setFont(font)
        self.user_status.setStyleSheet("color: rgb(95, 85, 100);\n"
"")
        self.user_status.setText("")
        self.user_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_status.setObjectName("user_status")
        self.verticalLayout_5.addWidget(self.user_status)
        self.verticalLayout_4.addWidget(self.widget_user)
        self.stackedWidget_sms = QtWidgets.QStackedWidget(self.widget_right_main)
        self.stackedWidget_sms.setObjectName("stackedWidget_sms")
        self.stackedWidget_smsPage1 = QtWidgets.QWidget()
        self.stackedWidget_smsPage1.setObjectName("stackedWidget_smsPage1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.stackedWidget_smsPage1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.stackedWidget_smsPage1)
        self.scrollArea.setStyleSheet("border: 1px solid transparent; /* Установка прозрачной границы */\n"
"    background-color: rgb(64, 57, 101);\n"
"    color: rgb(255, 255, 255);\n"
"QScrollArea {\n"
"    border: 1px solid transparent; /* Установка прозрачной границы */\n"
"    background-color: rgb(64, 57, 101);\n"
"    color: rgb(255, 255, 255);\n"
"    wight: 5px;\n"
"}\n"
"QScrollBar:vertical {\n"
"background: #2f2f2f;\n"
"width: 15px;\n"
"margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background: #5b5b5b;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"height: 0px;\n"
"}\n"
"")
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 417, 576))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sms_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sms_label.sizePolicy().hasHeightForWidth())
        self.sms_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sms_label.setFont(font)
        self.sms_label.setStyleSheet("background-color: rgb(64, 57, 101);\n"
"color: rgb(255, 255, 255);")
        self.sms_label.setText("")
        self.sms_label.setTextFormat(QtCore.Qt.AutoText)
        self.sms_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.sms_label.setObjectName("sms_label")
        self.horizontalLayout_5.addWidget(self.sms_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.stackedWidget_sms.addWidget(self.stackedWidget_smsPage1)
        self.page_info = QtWidgets.QWidget()
        self.page_info.setStyleSheet("background-color: rgb(64, 57, 101);\n"
"color: rgb(255, 255, 255);")
        self.page_info.setObjectName("page_info")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_info)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.page_info)
        self.label.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label.setStyleSheet("background-color: rgb(64, 57, 101);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.stackedWidget_sms.addWidget(self.page_info)
        self.verticalLayout_4.addWidget(self.stackedWidget_sms)
        self.widget_send_text = QtWidgets.QWidget(self.widget_right_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_send_text.sizePolicy().hasHeightForWidth())
        self.widget_send_text.setSizePolicy(sizePolicy)
        self.widget_send_text.setObjectName("widget_send_text")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_send_text)
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.send_text = QtWidgets.QTextEdit(self.widget_send_text)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_text.sizePolicy().hasHeightForWidth())
        self.send_text.setSizePolicy(sizePolicy)
        self.send_text.setStyleSheet("color: rgba(255, 255, 255,1);\n"
"border: transparent;")
        self.send_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_text.setAcceptRichText(False)
        self.send_text.setObjectName("send_text")
        self.horizontalLayout_4.addWidget(self.send_text)
        self.btn_send = QtWidgets.QPushButton(self.widget_send_text)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_send.setFont(font)
        self.btn_send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_send.setStyleSheet("QPushButton {\n"
"    border: 0px solid rgba(62, 63, 70, 0);\n"
"    border-radius: 0px;\n"
"    image: url(GUI/icons/send.png);\n"
"}\n"
"")
        self.btn_send.setText("")
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout_4.addWidget(self.btn_send)
        self.verticalLayout_4.addWidget(self.widget_send_text, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.widget_right_main)
        self.verticalLayout_2.addWidget(self.widget_main)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_sms.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Месседжер"))
        self.name_user.setText(_translate("MainWindow", "user name"))
        self.label_12.setText(_translate("MainWindow", "Создать группу     "))
        self.label_11.setText(_translate("MainWindow", "Контакты     "))
        self.label_9.setText(_translate("MainWindow", "Звонки     "))
        self.label_8.setText(_translate("MainWindow", "Настройки     "))
        self.label_7.setText(_translate("MainWindow", "Выйти     "))
        self.app_text.setText(_translate("MainWindow", "KFU Desktop Messaging"))
        self.app_text_2.setText(_translate("MainWindow", "Версия 0.1 - О программе "))
        self.search_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;\"><br /></p></body></html>"))
        self.search_text.setPlaceholderText(_translate("MainWindow", "Поиск"))
        self.label.setText(_translate("MainWindow", "Выберите, кому хотели бы написать"))
        self.send_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;\"><br /></p></body></html>"))
        self.send_text.setPlaceholderText(_translate("MainWindow", "Введите сообщение..."))
        self.btn_send.setShortcut(_translate("MainWindow", "Return"))
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
