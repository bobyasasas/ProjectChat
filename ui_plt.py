# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plt.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)
from qfluentwidgets import PushButton


class Ui_Plot(object):
    def setupUi(self, Plot):
        if not Plot.objectName():
            Plot.setObjectName(u"Plot")
        Plot.resize(607, 459)
        self.horizontalLayoutWidget = QWidget(Plot)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(80, 140, 431, 161))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_message = PushButton(self.horizontalLayoutWidget)
        self.pushButton_message.setObjectName(u"pushButton_message")
        font = QFont()
        font.setPointSize(14)
        self.pushButton_message.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_message)

        self.pushButton_user = PushButton(self.horizontalLayoutWidget)
        self.pushButton_user.setObjectName(u"pushButton_user")
        self.pushButton_user.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_user)


        self.retranslateUi(Plot)

        QMetaObject.connectSlotsByName(Plot)
    # setupUi

    def retranslateUi(self, Plot):
        Plot.setWindowTitle(QCoreApplication.translate("Plot", u"Form", None))
        self.pushButton_message.setText(QCoreApplication.translate("Plot", u"Message Plt", None))
        self.pushButton_user.setText(QCoreApplication.translate("Plot", u"User Plt", None))
    # retranslateUi

