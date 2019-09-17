# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\Subjects\A2 Computing\CG4\MonkeyStudio\Music System\mainwindow.ui'
#
# Created: Tue Oct  6 14:12:20 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(501, 371)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 140, 401, 191))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Main_MerchButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Main_MerchButton.setFont(font)
        self.Main_MerchButton.setObjectName(_fromUtf8("Main_MerchButton"))
        self.horizontalLayout.addWidget(self.Main_MerchButton)
        self.Main_MusicButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Main_MusicButton.setFont(font)
        self.Main_MusicButton.setObjectName(_fromUtf8("Main_MusicButton"))
        self.horizontalLayout.addWidget(self.Main_MusicButton)
        self.Main_PeopleButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Main_PeopleButton.setFont(font)
        self.Main_PeopleButton.setObjectName(_fromUtf8("Main_PeopleButton"))
        self.horizontalLayout.addWidget(self.Main_PeopleButton)
        self.Main_MainMenuText = QtGui.QLabel(self.centralwidget)
        self.Main_MainMenuText.setGeometry(QtCore.QRect(5, 70, 491, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Main_MainMenuText.setFont(font)
        self.Main_MainMenuText.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_MainMenuText.setObjectName(_fromUtf8("Main_MainMenuText"))
        self.Main_Logo = QtGui.QGraphicsView(self.centralwidget)
        self.Main_Logo.setGeometry(QtCore.QRect(90, 40, 81, 81))
        self.Main_Logo.setObjectName(_fromUtf8("Main_Logo"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.Main_MusicButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.MusicMenuButton)
        QtCore.QObject.connect(self.Main_MerchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.MerchandiseMenuButton)
        QtCore.QObject.connect(self.Main_PeopleButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.PeopleMenuButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Form1", None))
        self.Main_MerchButton.setText(_translate("MainWindow", "merchandise", None))
        self.Main_MusicButton.setText(_translate("MainWindow", "music", None))
        self.Main_PeopleButton.setText(_translate("MainWindow", "people", None))
        self.Main_MainMenuText.setText(_translate("MainWindow", "main menu", None))
        self.Main_Logo.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Tooltip test</span></p></body></html>", None))

