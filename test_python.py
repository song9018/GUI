# coding=utf-8
import sys

from PyQt4 import QtGui,QtCore
from PyQt4.Qt import *
from main_window import Ui_MainWindow
import ch
from dialog_input import Ui_Form1
ch.set_ch()

class child(QtGui.QWidget,Ui_Form1):
    _translate = QtCore.QCoreApplication.translate
    closeWidget = pyqtSignal()
    def __init__(self):
        super(child, self).__init__()
        self.setupUi(self)
        palette = QtGui.QPalette()
        icon = QtGui.QPixmap("./img/17_big.png")
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))  # 添加背景图片
        self.setPalette(palette)
        self.is_max = False
        self.setWindowFlags(Qt.FramelessWindowHint)  #
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.FramelessWindowHint)  #
        self.location = self.geometry()  #
        self.closeWidget.connect(self.close)


class window1(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(window1, self).__init__()
        self.setupUi(self)  # 加载窗体

    @QtCore.pyqtSlot()
    def on_pushButton1_clicked(self):
        self.a = child()
        self.a.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    aw = window1()
    aw.show()
    app.installEventFilter(aw)
    sys.exit(app.exec_())