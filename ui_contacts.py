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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidgetItem, QSizePolicy,
                               QWidget)

from qfluentwidgets import (ListWidget, PushButton)


class Ui_Contacts_Form(object):
    def setupUi(self, Contacts_Form):
        if not Contacts_Form.objectName():
            Contacts_Form.setObjectName(u"Contacts_Form")
        Contacts_Form.resize(800, 600)
        self.widget = QWidget(Contacts_Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(230, 10, 521, 431))
        self.pushButton_add_contact = PushButton(self.widget)
        self.pushButton_add_contact.setObjectName(u"pushButton_add_contact")
        self.pushButton_add_contact.setGeometry(QRect(350, 40, 91, 41))
        self.layoutWidget = QWidget(Contacts_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 10, 181, 521))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = ListWidget(self.layoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"listWidget{\n"
                                      "	background-color: rgb(238, 238, 238);\n"
                                      "}")

        self.horizontalLayout.addWidget(self.listWidget)

        self.retranslateUi(Contacts_Form)

        QMetaObject.connectSlotsByName(Contacts_Form)

    # setupUi

    def retranslateUi(self, Contacts_Form):
        Contacts_Form.setWindowTitle(QCoreApplication.translate("Contacts_Form", u"Form", None))
        self.pushButton_add_contact.setText(
            QCoreApplication.translate("Contacts_Form", u"\u6dfb\u52a0\u597d\u53cb", None))
    # retranslateUi
