# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'func.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from qfluentwidgets import PushButton


class Ui_Form_func(object):
    def setupUi(self, Form_func):
        if not Form_func.objectName():
            Form_func.setObjectName(u"Form_func")
        Form_func.resize(800, 600)
        self.verticalLayoutWidget = QWidget(Form_func)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 80, 774, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = PushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = PushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = PushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form_func)

        QMetaObject.connectSlotsByName(Form_func)
    # setupUi

    def retranslateUi(self, Form_func):
        Form_func.setWindowTitle(QCoreApplication.translate("Form_func", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form_func", u"flume", None))
        self.label.setText(QCoreApplication.translate("Form_func", u"we save messages by using flume, click to open it", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form_func", u"backup", None))
        self.label_2.setText(QCoreApplication.translate("Form_func", u"we back up mysql by using sqoop, click to back up", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form_func", u"sqoop", None))
        self.label_3.setText(QCoreApplication.translate("Form_func", u"click to open sqoop backup", None))
    # retranslateUi

