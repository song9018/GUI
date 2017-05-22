# coding=utf-8
import sys
import os
from PyQt4 import QtCore, QtGui, QtWebKit
from main_window import Ui_MainWindow
from PyQt4.Qt import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import ch, math
import function
from lon_lat import jiazao, ori_file, gps_handle_data
from dialog_input import Ui_Form1
from dialog_input_server import Ui_Form as server_ui_form
from analysisLocalTrack import oridatafile_transform

"""解决绘图中文显示问题"""
ch.set_ch()

"""初始化绘图参数"""


class plot(FigureCanvas):
    def __init__(self, parent=None, width=15, height=8, dpi=60):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_autoscale_on(False)

        self.axes.set_xlabel(window.x3, fontsize=18).set_color("g")
        self.axes.set_ylabel(window.y1, fontsize=18).set_color("r")
        self.axes2 = self.axes.twinx()
        self.axes2.set_ylabel(window.y2, fontsize=18).set_color("r")

        self.axes.grid(color='black', linestyle='-', linewidth=1)


        self.compute_initial_figure()
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


"""绘图内容设计"""


class plot_show(plot):
    list = []

    def __init__(self):
        super(plot_show, self).__init__()

    def compute_initial_figure(self):
        if window.x3 == u"时间(s)":
            self.axes.set_xticks(range(0, len(window.list_all[0]), int(math.ceil(len(window.list_all[0]) / 20))))

        if window.x3 == u"距离(km)":
            self.axes.set_xticks(np.arange(0, 10, 0.5))

        if window.XL and not window.XL_2:
            self.axes.set_yticks(range(0, 250, 10))
            self.plot_heart()
            window.XL = False
        if window.XL_2 and not window.XL:
            self.axes2.set_yticks(range(0, 250, 10))
            self.plot_heart()
            window.XL_2 = False
        if window.XL_2 and window.XL:
            self.axes.set_yticks(range(0, 250, 10))
            self.axes2.set_yticks(range(0, 250, 10))
            self.plot_heart()
            window.XL = False
            window.XL_2 = False

        if window.BP:
            self.axes.set_yticks(range(0, 250, 10))
        if window.BP_2:
            self.axes2.set_yticks(range(0, 250, 10))

        if window.SPEED:
            self.axes.set_yticks(range(0, 110, 10))
        if window.SPEED_2:
            self.axes2.set_yticks(range(0, 110, 10))

        if window.SPEED_RATE:
            self.axes.set_yticks(range(0, 250, 10))
        if window.SPEED_RATE_2:
            self.axes2.set_yticks(range(0, 250, 10))

        window.BP = False
        window.BP_2 = False
        window.SPEED = False
        window.SPEED_2 = False
        window.SPEED_RATE = False
        window.SPEED_RATE_2 = False
        self.axes.legend()

    def plot_heart(self):
        for i in range(len(window.list_tcx)):
            if window.list_tcx[i] == u"XLD":
                self.XLD, = self.axes.plot(np.arange(0, len(window.xld_heart), 1), window.xld_heart, label=u"心率带")
            if window.list_tcx[i] == u"XH3":
                self.XH3, = self.axes.plot(np.arange(0, len(window.xh3_heart), 1), window.xh3_heart, label=u"XH3")
            if window.list_tcx[i] == u"NOW2":
                self.NOW2, = self.axes.plot(np.arange(0, len(window.now2_heart), 1), window.now2_heart, label=u"NOW2")
            if window.list_tcx[i] == u"MTK2511":
                self.MTK, = self.axes.plot(np.arange(0, len(window.mtk_heart), 1), window.mtk_heart, label=u"MTK")
            if window.list_tcx[i] == u"COROS":
                self.COROS, = self.axes.plot(np.arange(0, len(window.coros_heart), 1), window.coros_heart,
                                             label=u"COROS")


"""html文件写入"""


class Lat_Lon(object):
    def write_lat_lon(self, file_name, list1, list2=None, list3=None):
        file = open(file_name, 'r')
        list = file.readlines()
        len_t = len(list) - 1
        for i in range(len_t):
            if "center" in list[i]:
                data = list[i].split(':')[1]
                list[i] = list[i].replace(data, str(list1[0]) + ",\n")

            if 'var lineArr' in list[i]:
                data = list[i].split('=')[1]
                list[i] = list[i].replace(data, str(list1) + "\n")

            if 'var lineArr1' in list[i]:
                data = list[i].split('=')[1]
                list[i] = list[i].replace(data, str(list2) + "\n")
            if 'var lineArr2' in list[i]:
                data = list[i].split('=')[1]
                list[i] = list[i].replace(data, str(list3) + "\n")

        file = open(file_name, 'w')
        file.writelines(list)


"""地图加载"""


class BrowserScreen(QtWebKit.QWebView):
    def __init__(self, file_name):
        QWebView.__init__(self)
        self.resize(800, 600)
        self.setUrl(QUrl(os.path.join(os.getcwd(), file_name)))


"""程序主窗口加载"""


class window(QMainWindow, Ui_MainWindow):
    XL, XL_2, BP, BP_2, SPEED, SPEED_2, SPEED_RATE, SPEED_RATE_2 = False, False, False, False, False, False, False, False
    i, j, k, check_id = 0, 0, 0, 0
    list_all = []

    _translate = QtCore.QCoreApplication.translate
    closeWidget = pyqtSignal()

    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)  # 加载窗体

        palette = QtGui.QPalette()
        icon = QtGui.QPixmap("./img/17_big.png")
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))  # 添加背景图片
        self.setPalette(palette)
        self.is_max = False
        self.setWindowFlags(Qt.FramelessWindowHint)  #
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.FramelessWindowHint)  #
        self.location = self.geometry()  #
        self.closeWidget.connect(self.close)
        self.run_map("./build/handle_none.html")

    """设置鼠标拖动"""

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    """错误弹框设置"""

    def Massage(self):
        reply = QtGui.QMessageBox.warning(self, u"警告", u"选择文件有误，请重新选择", QMessageBox.Ok | QMessageBox.Cancel)

    def Massage1(self):
        reply = QtGui.QMessageBox.warning(self, u"程序出错", u"未知错误，请重新操作", QMessageBox.Ok | QMessageBox.Cancel)

    """加载地图 """

    def run_map(self, file_name):
        sc = BrowserScreen(file_name)
        graphicscene = QGraphicsScene()
        graphicscene.addWidget(sc)
        self.graphicsView_2.setScene(graphicscene)
        self.graphicsView_2.show()

    """加载心率图表"""

    def run_heart(self):
        sc = plot_show()
        graphicscene = QtGui.QGraphicsScene()
        graphicscene.addWidget(sc)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()

    # 最小化按钮
    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        self.showMinimized()

    # 关闭按钮
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.close()

        # @pyqtSlot()
        # def on_pushButton_2_clicked(self):
        #     if not self.isMaximized():
        #         self.showMaximized()
        #     else:
        #         self.showNormal()

    # 心率文件、GPS文件选择
    @pyqtSlot()
    def on_pushButton_4_clicked(self):

        try:
            fileName = QFileDialog.getOpenFileNames(self, u"选取文件", "", options=QFileDialog.DontUseNativeDialog)
            self.heart_add_list(unicode(fileName[0]))
            self.gps_ori_add_list(unicode(fileName[0]))
            window.ori_latlon = self.add_gps(oridatafile_transform(unicode(fileName[0])))
            print window.ori_latlon
            if window.ori_latlon:
                self.gps_ori_list(unicode(fileName[0]))
        except Exception as e:
            print e

    # 轨迹文件原始数据文件
    def gps_ori_add_list(self, fileName):
        try:
            window.latlon_list = self.add_gps(ori_file(fileName))

        except Exception as e:
            print e

    # 轨迹文件原始数据文件
    def gps_ori_list(self, fileName):
        try:
            path = fileName.split("/")[-1]
            self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
            self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                "MainWindow", "xh3s_gps", None,
                QtGui.QApplication.UnicodeUTF8))

            self.item_1.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

            self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
            self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
                                                                                    QtGui.QApplication.translate(
                                                                                        "MainWindow", path,
                                                                                        None,
                                                                                        QtGui.QApplication.UnicodeUTF8))
            self.item_2.setCheckState(0, QtCore.Qt.Checked)
            window.check_id += 1

        except Exception as e:
            print e

    # 轨迹文件算法处理
    def gps_handle_add_list(self, fileName):
        try:
            latlon_list = self.add_gps(gps_handle_data(fileName))
            return latlon_list
        except Exception as e:
            print e

    # 心率文件提取心率处理
    def heart_add_list(self, fileName):
        try:
            file = open(fileName, "r")
            path = fileName.split("/")[-1]
            ppg = function.func(fileName)
            for line in file.readlines():
                if " BLE1" in line or " Pol" in line:
                    window.xld_time, window.xld_heart = ppg.XLD()
                    window.list_all.append(window.xld_heart)
                    self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
                    self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                        "MainWindow", "XLD", None,
                        QtGui.QApplication.UnicodeUTF8))

                    self.item_1.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

                    self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
                    self.treeWidget.topLevelItem(0).child(0).child(0).setText(0,
                                                                              QtGui.QApplication.translate(
                                                                                  "MainWindow", path,
                                                                                  None,
                                                                                  QtGui.QApplication.UnicodeUTF8))
                    self.item_2.setCheckState(0, QtCore.Qt.Checked)
                    window.check_id += 1
                    break
                if 'HR:***' in line:
                    window.xh3_time, window.xh3_heart = ppg.XH3()
                    window.list_all.append(window.xh3_heart)
                    self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
                    self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                        "MainWindow", "XH3", None,
                        QtGui.QApplication.UnicodeUTF8))

                    self.item_1.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

                    self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
                    self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
                                                                                            QtGui.QApplication.translate(
                                                                                                "MainWindow", path,
                                                                                                None,
                                                                                                QtGui.QApplication.UnicodeUTF8))
                    self.item_2.setCheckState(0, QtCore.Qt.Checked)
                    window.check_id += 1
                    break
                if '][' in line:
                    window.now2_time, window.now2_heart = ppg.NOW2()
                    window.list_all.append(window.now2_heart)
                    self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
                    self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                        "MainWindow", "NOW2", None,
                        QtGui.QApplication.UnicodeUTF8))

                    self.item_1.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

                    self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
                    self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
                                                                                            QtGui.QApplication.translate(
                                                                                                "MainWindow", path,
                                                                                                None,
                                                                                                QtGui.QApplication.UnicodeUTF8))
                    self.item_2.setCheckState(0, QtCore.Qt.Checked)
                    window.check_id += 1
                    break

                if '22,0,' in line:
                    window.mtk_time, window.mtk_heart = ppg.MTK2511()
                    window.list_all.append(window.mtk_heart)
                    self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
                    self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                        "MainWindow", "MTK2511", None,
                        QtGui.QApplication.UnicodeUTF8))

                    self.item_1.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

                    self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
                    self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
                                                                                            QtGui.QApplication.translate(
                                                                                                "MainWindow", path,
                                                                                                None,
                                                                                                QtGui.QApplication.UnicodeUTF8))
                    self.item_2.setCheckState(0, QtCore.Qt.Checked)
                    window.check_id += 1
                    break

                if 'RX' in line:
                    window.coros_time, window.coros_heart = ppg.COROS()
                    window.list_all.append(window.coros_heart)
                    self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
                    self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                        "MainWindow", "COROS", None,
                        QtGui.QApplication.UnicodeUTF8))

                    self.item_1.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

                    self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
                    self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
                                                                                            QtGui.QApplication.translate(
                                                                                                "MainWindow", path,
                                                                                                None,
                                                                                                QtGui.QApplication.UnicodeUTF8))
                    self.item_2.setCheckState(0, QtCore.Qt.Checked)
                    window.check_id += 1
                    break

                if '0.000000 0.000000' in line:
                    self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
                    self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                        "MainWindow", "gps_file", None,
                        QtGui.QApplication.UnicodeUTF8))

                    self.item_1.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

                    self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
                    self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
                                                                                            QtGui.QApplication.translate(
                                                                                                "MainWindow", path,
                                                                                                None,
                                                                                                QtGui.QApplication.UnicodeUTF8))
                    self.item_2.setCheckState(0, QtCore.Qt.Checked)
                    window.check_id += 1
                    break
                    # self.wlp.heart_wlp()
                    # for i in range(len(window.xld_time)):
                    #     self.wlp.add_activity("XH3", str(window.xld_time[i]), str(window.xld_heart[i]))
                    #     self.wlp.close_file()

        except Exception as e:
            print e

    # 心率图表绘图按钮
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        try:
            window.list_tcx = []

            window.y1 = self.comboBox_3.currentText()
            window.y2 = self.comboBox_2.currentText()
            window.x3 = self.comboBox_4.currentText()

            if window.y1 == u"心率(bpm)":
                window.XL = True
            if window.y1 == u"步频(spm)":
                window.BP = True
            if window.y1 == u"速度(km/h)":
                window.SPEED = True
            if window.y1 == u"配速(min/km)":
                window.SPEED_RATE = True

            if window.y2 == u"心率(bpm)":
                window.XL_2 = True
            if window.y2 == u"步频(spm)":
                window.BP_2 = True
            if window.y2 == u"速度(km/h)":
                window.SPEED_2 = True
            if window.y2 == u"配速(min/km)":
                window.SPEED_RATE_2 = True
            try:
                for i in range(10):
                    if self.treeWidget.topLevelItem(0).child(i).checkState(0) == QtCore.Qt.Checked:
                        window.list_tcx.append(str(self.treeWidget.topLevelItem(0).child(i).text(0)))

            except Exception as e:
                print e
            finally:
                self.get_time()
                sc = plot_show()
                graphicscene = QtGui.QGraphicsScene()
                graphicscene.addWidget(sc)
                self.graphicsView.setScene(graphicscene)
                self.graphicsView.show()
        except Exception as e:
            print e

    # 高德轨迹图加载按钮
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        latlon = Lat_Lon()
        window.list_gps = []
        k = 0
        try:
            for i in range(10):
                if self.treeWidget.topLevelItem(0).child(i).checkState(0) == QtCore.Qt.Checked:
                    window.list_gps.append(str(self.treeWidget.topLevelItem(0).child(i).text(0)))

        except Exception as e:
            print e
        finally:
            for i in range(len(window.list_gps)):
                if window.list_gps[i] == "add_voice":
                    latlon.write_lat_lon(file_name="./build/handle.html", list1=child_add_voice.add_latlon_list)
                    self.run_map("./build/handle.html")
                    k += 1
                elif window.list_gps[i] == "handle_gps":
                    latlon.write_lat_lon(file_name="./build/handle.html", list1=window.handle_gps)
                    self.run_map("./build/handle.html")
                    k += 1
                elif window.list_gps[i] == "gps_file":
                    latlon.write_lat_lon(file_name="./build/handle.html", list1=window.latlon_list)
                    self.run_map("./build/handle.html")
                    k += 1
                elif window.list_gps[i] == "xh3s_gps":
                    latlon.write_lat_lon(file_name="./build/handle.html",list1=window.ori_latlon)
                    print window.ori_latlon
                    self.run_map("./build/handle.html")
                    k += 1
            if k == 0:
                self.run_map("./build/handle_none.html")

    # 加噪输入弹框按钮
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        try:
            window.fileName = QFileDialog.getOpenFileNames(self, u"选取文件", "", options=QFileDialog.DontUseNativeDialog)
            path = window.fileName[0].split("/")[-1]
            self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
            self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                "MainWindow", "add_voice", None,
                QtGui.QApplication.UnicodeUTF8))

            self.item_1.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

            self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
            self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
                                                                                    QtGui.QApplication.translate(
                                                                                        "MainWindow", path,
                                                                                        None,
                                                                                        QtGui.QApplication.UnicodeUTF8))
            self.item_2.setCheckState(0, QtCore.Qt.Checked)
            window.check_id += 1

            # 加载对话框
            self.a = child_add_voice()
            self.a.show()
        except Exception as e:
            print e

    # 算法处理加载按钮
    @pyqtSlot()
    def on_pushButton_11_clicked(self):
        """

        处理加噪--算法处理？？？
        :return:
        """

        try:
            fileName = QFileDialog.getOpenFileNames(self, u"选取文件", "", options=QFileDialog.DontUseNativeDialog)
            path = fileName[0].split("/")[-1]
            self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
            self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
                "MainWindow", "handle_gps", None,
                QtGui.QApplication.UnicodeUTF8))

            self.item_1.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

            self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
            self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
                                                                                    QtGui.QApplication.translate(
                                                                                        "MainWindow", path,
                                                                                        None,
                                                                                        QtGui.QApplication.UnicodeUTF8))
            self.item_2.setCheckState(0, QtCore.Qt.Checked)
            window.check_id += 1

            # 算法处理
            window.handle_gps = self.gps_handle_add_list(unicode(fileName[0]))
        except Exception as e:
            print e

    # 服务器轨迹文件下载处理
    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        self.a = child_download()
        self.a.show()
        # self.item_1 = QtGui.QTreeWidgetItem(self.item_0)
        # self.treeWidget.topLevelItem(0).child(window.check_id).setText(0, QtGui.QApplication.translate(
        #     "MainWindow", "service_gps", None,
        #     QtGui.QApplication.UnicodeUTF8))
        #
        # self.item_1.setFlags(
        #     QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)
        #
        # self.item_2 = QtGui.QTreeWidgetItem(self.item_1)
        # self.treeWidget.topLevelItem(0).child(window.check_id).child(0).setText(0,
        #                                                                         QtGui.QApplication.translate(
        #                                                                             "MainWindow", "download_file",
        #                                                                             None,
        #                                                                             QtGui.QApplication.UnicodeUTF8))
        # self.item_2.setCheckState(0, QtCore.Qt.Checked)
        # window.check_id += 1

    # GPS偏移设置
    def add_gps(self, list1):
        for i in range(len(list1)):
            list1[i][0] = list1[i][0] + 0.004843
            list1[i][1] = list1[i][1] - 0.002995
        return list1


    def get_time(self):
        t1=0
        for i in range(len(window.list_tcx)):
            if window.list_tcx[i] == u"XH3":
                for i in range(len(window.xh3_heart)):
                    if window.xh3_heart[i]=="0" or window.xh3_heart[i]=="":
                        t1+=1
                pol_heart_time = QTableWidgetItem("wew")
                pol_time = QTableWidgetItem("asdasd")
                self.tableWidget.setItem(0, 0, t1)
                self.tableWidget.setItem(0, 1, pol_time)



"""加噪对话框加载"""


class child_add_voice(QtGui.QWidget, Ui_Form1):
    _translate = QtCore.QCoreApplication.translate
    closeWidget = pyqtSignal()

    def __init__(self):
        super(child_add_voice, self).__init__()
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

    # 设置鼠标拖动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    @pyqtSlot()
    def on_pushButton_dialog_clicked(self):
        child_add_voice.input = str(self.lineEdit.text())
        self.gps_add_list(unicode(window.fileName[0]))
        self.close()

    @pyqtSlot()
    def on_pushButton_dialog_2_clicked(self):
        self.close()

    @pyqtSlot()
    def on_pushButton_dialog_3_clicked(self):
        self.close()

    # 轨迹文件加噪处理
    def gps_add_list(self, fileName):
        try:
            input = child_add_voice.input
            distance = float(input.split()[0])
            number = int(input.split()[1])
            latlon_list = jiazao(distance, number, fileName)
            child_add_voice.add_latlon_list = self.add_gps(latlon_list)

        except Exception as e:
            print e

    """
     GPS偏移量设置
     """

    def add_gps(self, list1):
        for i in range(len(list1)):
            list1[i][0] = list1[i][0] + 0.004843
            list1[i][1] = list1[i][1] - 0.002995
        return list1


"""服务器文件下载对话框加载"""


class child_download(QtGui.QWidget, server_ui_form):
    _translate = QtCore.QCoreApplication.translate
    closeWidget = pyqtSignal()

    def __init__(self):
        super(child_download, self).__init__()
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

    # 设置鼠标拖动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    # 输入框
    @pyqtSlot()
    def on_pushButton_dialog_server_clicked(self):
        child_download.input = str(self.lineEdit.text())
        self.close()

    # 取消按钮
    @pyqtSlot()
    def on_pushButton_dialog_server_2_clicked(self):
        self.close()

    # 关闭按钮
    @pyqtSlot()
    def on_pushButton_dialog_server_3_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    aw = window()
    aw.setWindowTitle(u"WeLoop测试工具")
    aw.show()
    app.installEventFilter(aw)
    sys.exit(app.exec_())
