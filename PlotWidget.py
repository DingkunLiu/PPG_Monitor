import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class PlotWidget(QtWidgets.QWidget):
    def __init__(self, nrow, ncol, parent=None):
        super(PlotWidget, self).__init__(parent)
        self.figure, self.axis = plt.subplots(nrows=nrow, ncols=ncol)

        self.canvas = FigureCanvasQTAgg(self.figure)

        self.layoutVertical = QtWidgets.QGridLayout(self)
        self.layoutVertical.addWidget(self.canvas)
