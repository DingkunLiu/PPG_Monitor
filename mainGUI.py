import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt

from PPG_Processor import PPG_Running
from myUI import Ui_MainWindow


class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # update interval
    updateinterval = .1

    def __init__(self):
        super(mainWindow, self).__init__()
        self.datakeeper = PPG_Running()
        self.setupUi(self)
        # set background color
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, Qt.white)
        self.setPalette(pal)
        # graph
        self.graph.line = self.graph.axis.plot([], [])[0]
        # timer for receive data
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.datacallback)

        # timer for update heart rate
        # update every 5 sec
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.updateVal)

        # connect button
        self.connect_Button.clicked.connect(self.connectbuttonSignal)
        self.Disconnect_Button.clicked.connect(self.disconnectSignal)
        self.Start_Measure_Button.clicked.connect(self.measurebuttonSignal)
        self.connect_Button_2.clicked.connect(self.HRVbuttonSignal)

    def connectbuttonSignal(self):
        self.datakeeper.reset_input_buffer()
        self.timer1.start(int(self.updateinterval * 1000))

    def HRVbuttonSignal(self):
        rate = self.datakeeper.HRV_analysis()
        rate_filted = signal.filtfilt(np.ones((5,)) / 5, 1, rate, method='pad')
        fig, ax = plt.subplots(2, 1)
        ax[0].plot(rate_filted)
        ax[1].hist(rate_filted, 40)
        fig.savefig('result.png')

    def measurebuttonSignal(self):
        self.timer2.start(1000)

    def disconnectSignal(self):
        self.timer1.stop()
        self.timer2.stop()
        self.datakeeper.reset_state()

    def datacallback(self):
        self.datakeeper.receive_data()
        dataforplot = self.datakeeper.databuffer
        x = np.linspace(0, len(dataforplot) / self.datakeeper.fs, len(dataforplot))
        self.graph.line.set_xdata(x)
        self.graph.line.set_ydata(dataforplot)
        self.graph.axis.relim()
        self.graph.axis.autoscale_view()
        self.graph.canvas.draw()

    def updateVal(self):
        hr = self.datakeeper.heart_rate()
        if hr >= 0:
            self.lcdNumber.display(hr)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = mainWindow()
    GUI.show()
    sys.exit(app.exec_())
