# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mcalderon/cursos/rob1/qtforms/myapp/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.priceEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.priceEdit.setGeometry(QtCore.QRect(140, 50, 104, 78))
        self.priceEdit.setObjectName("priceEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.taxrate = QtWidgets.QSpinBox(self.centralwidget)
        self.taxrate.setGeometry(QtCore.QRect(140, 140, 48, 27))
        self.taxrate.setProperty("value", 20)
        self.taxrate.setObjectName("taxrate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 67, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 180, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.resultWindow = QtWidgets.QTextEdit(self.centralwidget)
        self.resultWindow.setGeometry(QtCore.QRect(140, 220, 104, 78))
        self.resultWindow.setObjectName("resultWindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tax Calculator"))
        self.label_2.setText(_translate("MainWindow", "Price"))
        self.label_3.setText(_translate("MainWindow", "Tax Rate"))
        self.pushButton.setText(_translate("MainWindow", "Calculator tax"))

