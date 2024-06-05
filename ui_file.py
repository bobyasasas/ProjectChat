# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidgetItem, QSizePolicy, QWidget)

from qfluentwidgets import (ListWidget, PushButton)

class Ui_FILE(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(698, 605)
        self.pushButton_upload = PushButton(Form)
        self.pushButton_upload.setObjectName(u"pushButton_upload")
        self.pushButton_upload.setGeometry(QRect(60, 40, 111, 51))
        self.listWidget = ListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(60, 150, 591, 391))
        self.pushButton_flush = PushButton(Form)
        self.pushButton_flush.setObjectName(u"pushButton_flush")
        self.pushButton_flush.setGeometry(QRect(250, 40, 111, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_upload.setText(QCoreApplication.translate("Form", u"upload_file", None))
        self.pushButton_flush.setText(QCoreApplication.translate("Form", u"flush", None))
    # retranslateUi

