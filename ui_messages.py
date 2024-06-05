# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messages.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QScrollArea,
    QSizePolicy, QWidget)

from qfluentwidgets import (PlainTextEdit, PushButton,ScrollArea)

class Ui_Form_message(object):
    def setupUi(self, Form_message):
        if not Form_message.objectName():
            Form_message.setObjectName(u"Form_message")
        Form_message.resize(640, 480)
        self.widget = QWidget(Form_message)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 641, 481))
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 30, 641, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_send = PushButton(self.widget)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setGeometry(QRect(520, 420, 111, 31))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 0, 221, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plainTextEdit = PlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 330, 621, 81))
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 310, 641, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.widget_message = QWidget(self.widget)
        self.widget_message.setObjectName(u"widget_message")
        self.widget_message.setGeometry(QRect(10, 60, 621, 241))
        self.scrollArea = ScrollArea(self.widget_message)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, -10, 621, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 619, 249))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form_message)

        QMetaObject.connectSlotsByName(Form_message)
    # setupUi

    def retranslateUi(self, Form_message):
        Form_message.setWindowTitle(QCoreApplication.translate("Form_message", u"Form", None))
        self.pushButton_send.setText(QCoreApplication.translate("Form_message", u"\u53d1\u9001", None))
        self.label.setText(QCoreApplication.translate("Form_message", u"kai", None))
    # retranslateUi

