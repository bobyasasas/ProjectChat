# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signin.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CaptionLabel, LineEdit, PasswordLineEdit, PrimaryPushButton,
    TransparentPushButton)

class Ui_signin_window(object):
    def setupUi(self, signin_window):
        if not signin_window.objectName():
            signin_window.setObjectName(u"signin_window")
        signin_window.resize(396, 501)
        self.layoutWidget = QWidget(signin_window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 40, 281, 351))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = CaptionLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setWindowModality(Qt.WindowModality.WindowModal)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setUnderline(False)
        self.line.setFont(font1)
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_username = LineEdit(self.layoutWidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.lineEdit_username)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.lineEdit_passwd = PasswordLineEdit(self.layoutWidget)
        self.lineEdit_passwd.setObjectName(u"lineEdit_passwd")
        self.lineEdit_passwd.setMinimumSize(QSize(0, 0))
        self.lineEdit_passwd.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setWeight(QFont.Thin)
        self.lineEdit_passwd.setFont(font2)
        self.lineEdit_passwd.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.lineEdit_passwd)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_signin = PrimaryPushButton(self.layoutWidget)
        self.pushButton_signin.setObjectName(u"pushButton_signin")
        font3 = QFont()
        font3.setPointSize(17)
        self.pushButton_signin.setFont(font3)

        self.verticalLayout_4.addWidget(self.pushButton_signin)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_login = TransparentPushButton(self.layoutWidget)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.horizontalLayout.addWidget(self.pushButton_login)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_forget = TransparentPushButton(self.layoutWidget)
        self.pushButton_forget.setObjectName(u"pushButton_forget")

        self.horizontalLayout.addWidget(self.pushButton_forget)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.retranslateUi(signin_window)

        QMetaObject.connectSlotsByName(signin_window)
    # setupUi

    def retranslateUi(self, signin_window):
        signin_window.setWindowTitle(QCoreApplication.translate("signin_window", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("signin_window", u"\u767b\u5f55", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_username.setToolTip(QCoreApplication.translate("signin_window", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_username.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit_username.setInputMask("")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("signin_window", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.lineEdit_passwd.setText("")
        self.lineEdit_passwd.setPlaceholderText(QCoreApplication.translate("signin_window", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton_signin.setText(QCoreApplication.translate("signin_window", u"\u767b\u5f55", None))
        self.pushButton_login.setText(QCoreApplication.translate("signin_window", u"\u73b0\u5728\u6ce8\u518c", None))
        self.pushButton_forget.setText(QCoreApplication.translate("signin_window", u"\u5fd8\u8bb0\u5bc6\u7801?", None))
    # retranslateUi

