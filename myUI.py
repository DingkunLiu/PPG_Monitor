# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PPG.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setScaledContents(False)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 70.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.graph = PlotWidget(1, 1, self.layoutWidget)
        self.graph.setObjectName("graph")
        self.gridLayout.addWidget(self.graph, 1, 0, 1, 1)
        self.Start_Measure_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Start_Measure_Button.setObjectName("Start_Measure_Button")
        self.gridLayout.addWidget(self.Start_Measure_Button, 5, 0, 1, 1)
        self.Disconnect_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Disconnect_Button.setObjectName("Disconnect_Button")
        self.gridLayout.addWidget(self.Disconnect_Button, 5, 2, 1, 1)
        self.connect_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.connect_Button.setObjectName("connect_Button")
        self.gridLayout.addWidget(self.connect_Button, 4, 2, 1, 1)
        self.connect_Button_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.connect_Button_2.setObjectName("connect_Button_2")
        self.gridLayout.addWidget(self.connect_Button_2, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 26))
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
        self.title.setText(_translate("MainWindow", "PPG Monitor"))
        self.label.setText(_translate("MainWindow", "Heart Rate:"))
        self.Start_Measure_Button.setText(_translate("MainWindow", "Start Measure"))
        self.Disconnect_Button.setText(_translate("MainWindow", "Pause"))
        self.connect_Button.setText(_translate("MainWindow", "Start"))
        self.connect_Button_2.setText(_translate("MainWindow", "HRV"))

from PlotWidget import PlotWidget
