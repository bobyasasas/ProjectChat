# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts.ui'
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

class Ui_Contacts_Form(object):
    def setupUi(self, Contacts_Form):
        if not Contacts_Form.objectName():
            Contacts_Form.setObjectName(u"Contacts_Form")
        Contacts_Form.resize(800, 600)
        self.listWidget = ListWidget(Contacts_Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 40, 411, 531))
        self.pushButton_add_contact = PushButton(Contacts_Form)
        self.pushButton_add_contact.setObjectName(u"pushButton_add_contact")
        self.pushButton_add_contact.setGeometry(QRect(460, 50, 160, 60))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_add_contact.setFont(font)
        self.pushButton_del_contact = PushButton(Contacts_Form)
        self.pushButton_del_contact.setObjectName(u"pushButton_del_contact")
        self.pushButton_del_contact.setGeometry(QRect(460, 140, 160, 60))
        self.pushButton_del_contact.setFont(font)

        self.retranslateUi(Contacts_Form)

        QMetaObject.connectSlotsByName(Contacts_Form)
    # setupUi

    def retranslateUi(self, Contacts_Form):
        Contacts_Form.setWindowTitle(QCoreApplication.translate("Contacts_Form", u"Form", None))
        self.pushButton_add_contact.setText(QCoreApplication.translate("Contacts_Form", u"add freinds", None))
        self.pushButton_del_contact.setText(QCoreApplication.translate("Contacts_Form", u"delete contact", None))
    # retranslateUi

