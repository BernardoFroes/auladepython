# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCommandLinkButton, QDialogButtonBox,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(300, 60, 641, 411))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.commandLinkButton_5 = QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_5.setObjectName(u"commandLinkButton_5")

        self.verticalLayout.addWidget(self.commandLinkButton_5)

        self.commandLinkButton = QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.verticalLayout.addWidget(self.commandLinkButton)

        self.commandLinkButton_2 = QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")

        self.verticalLayout.addWidget(self.commandLinkButton_2)

        self.commandLinkButton_3 = QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_3.setObjectName(u"commandLinkButton_3")

        self.verticalLayout.addWidget(self.commandLinkButton_3)

        self.commandLinkButton_4 = QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_4.setObjectName(u"commandLinkButton_4")

        self.verticalLayout.addWidget(self.commandLinkButton_4)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.radioButton = QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.commandLinkButton_5.setText(QCoreApplication.translate("MainWindow", u"Apostar R$ 5,00", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Apostar  R$10,00", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"Apostar  R$ 20,00", None))
        self.commandLinkButton_3.setText(QCoreApplication.translate("MainWindow", u"Apostar  R$ 50,00", None))
        self.commandLinkButton_4.setText(QCoreApplication.translate("MainWindow", u"Apostar  R$ 100,00", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Brasil (F) para vencer: 4.00", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Aceitar Mudan\u00e7as de Cota\u00e7\u00e3o", None))
    # retranslateUi

