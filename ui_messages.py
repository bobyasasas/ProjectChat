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
    QSizePolicy, QTextEdit, QWidget)

from qfluentwidgets import PushButton, ScrollArea, TextEdit


class Ui_Form_message(object):
    def setupUi(self, Form_message):
        if not Form_message.objectName():
            Form_message.setObjectName(u"Form_message")
        Form_message.resize(373, 618)
        self.widget = QWidget(Form_message)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 371, 541))
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 30, 391, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 0, 221, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_message = QWidget(self.widget)
        self.widget_message.setObjectName(u"widget_message")
        self.widget_message.setGeometry(QRect(10, 60, 621, 301))
        self.scrollArea = ScrollArea(self.widget_message)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, -10, 351, 301))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 349, 299))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textEdit = TextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 380, 351, 151))
        self.pushButton_send = PushButton(Form_message)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setGeometry(QRect(250, 550, 111, 31))

        self.retranslateUi(Form_message)

        QMetaObject.connectSlotsByName(Form_message)
    # setupUi

    def retranslateUi(self, Form_message):
        Form_message.setWindowTitle(QCoreApplication.translate("Form_message", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form_message", u"kai", None))
        self.pushButton_send.setText(QCoreApplication.translate("Form_message", u"\u53d1\u9001", None))
    # retranslateUi

