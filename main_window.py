# -*- coding: utf-8 -*-

"""
:param MainWindow:weloop test tool
:writer:song chuhua
"""

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        """
        主窗体设计
        """
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(998, 664)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(902, 664))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./img/weloop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        """
        文件列表选项设置
        """
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 90, 191, 541))
        self.treeWidget.setToolTip(
            QtGui.QApplication.translate("MainWindow", "数据文件", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setStyleSheet(_fromUtf8(""))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setIcon(0, icon1)



        """
        TCX文件列表设置
        """
        self.item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "数据文件", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        brush = QtGui.QBrush(QtGui.QColor(210, 244, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.item_0.setBackground(0, brush)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        """
        LOGO图标设计
        """
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 6, 101, 71))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./img/weloop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(71, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setStyleSheet("background:transparent")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 60, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "WeLoop", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setStyleSheet("color:white")

        """
        关闭按钮、最小化、最大化按钮设计
        """
        # self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(940, 4, 25, 23))
        # self.pushButton_2.setText(_fromUtf8(""))
        # icon3 = QtGui.QIcon()
        # icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./img/max.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton_2.setIcon(icon3)
        # self.pushButton_2.setIconSize(QtCore.QSize(25, 23))
        # self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        # self.pushButton_2.setStyleSheet("background:transparent")
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(970, 4, 25, 25))
        self.pushButton_3.setToolTip(
            QtGui.QApplication.translate("MainWindow", "关闭", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./img/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet("background:transparent")
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(940, 4, 25, 23))
        self.pushButton_1.setToolTip(
            QtGui.QApplication.translate("MainWindow", "最小化", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_1.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("./img/min.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon5)
        self.pushButton_1.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_1.setStyleSheet("background:transparent")

        """
        tab1窗体设计--心率
        """
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(190, 90, 809, 541))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-70, -20, 910, 605))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("img/heart.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_1, icon6, _fromUtf8(""))

        """
        绘图按钮设计
        """
        self.pushButton_7 = QtGui.QPushButton(self.tab_1)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 0, 40, 40))
        self.pushButton_7.setToolTip(
            QtGui.QApplication.translate("MainWindow", "生成图表", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(
            QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        icon12 = QtGui.QIcon()
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("./img/plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon12)

        """
        绘图X轴选项设计
        """
        self.comboBox_4 = QtGui.QComboBox(self.tab_1)
        self.comboBox_4.setGeometry(QtCore.QRect(360, 40, 70, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.setItemText(0, QtGui.QApplication.translate("MainWindow", "时间(s)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.setItemText(1, QtGui.QApplication.translate("MainWindow", "距离(km)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))

        """
        绘图Y轴选项设计
        """
        self.comboBox_3 = QtGui.QComboBox(self.tab_1)
        self.comboBox_3.setGeometry(QtCore.QRect(30, 10, 76, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("MainWindow", "心率(bpm)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("MainWindow", "步频(spm)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.setItemText(2, QtGui.QApplication.translate("MainWindow", "速度(km/h)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.setItemText(3, QtGui.QApplication.translate("MainWindow", "配速(min/km)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2 = QtGui.QComboBox(self.tab_1)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 10, 76, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("MainWindow", "心率(bpm)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("MainWindow", "步频(spm)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("MainWindow", "速度(km/h)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(3, QtGui.QApplication.translate("MainWindow", "配速(min/km)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))

        """
        tab2窗体设计--轨迹
        """
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("widget"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, -10, 811, 521))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.gridLayoutWidget_2)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.gridLayout_2.addWidget(self.graphicsView_2, 0, 0, 1, 1)
        """
        高德地图、百度地图--图标设计
        """
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 0, 30, 30))
        self.pushButton_6.setToolTip(
            QtGui.QApplication.translate("MainWindow", "高德地图", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(
            QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.setStyleSheet("background:transparent")
        icon13 = QtGui.QIcon()
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("./img/gaode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon13)

        self.pushButton_8 = QtGui.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(310, 0, 30,30))
        self.pushButton_8.setToolTip(
            QtGui.QApplication.translate("MainWindow", "百度地图", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(
            QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.setStyleSheet("background:transparent")
        icon14 = QtGui.QIcon()
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("./img/baidu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon14)
        """
        下载服务器轨迹文件等功能--下拉框设计
        """
        self.pushButton_9 = QtGui.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 0, 61, 31))
        self.pushButton_9.setText(
            QtGui.QApplication.translate("MainWindow", "添加噪声", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 0, 61, 31))
        self.pushButton_10.setText(
            QtGui.QApplication.translate("MainWindow", "下载文件", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))

        self.pushButton_11 = QtGui.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(135, 0, 61, 31))
        self.pushButton_11.setText(
            QtGui.QApplication.translate("MainWindow", "算法处理", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))


        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("img/map.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon7, _fromUtf8(""))

        """
        tab3窗体设计--数据统计
        """
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableWidget = QtGui.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 253, 209))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "XH3", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "NOW2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "8011-1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "8011-2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "MTK", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "COROS", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "出值时间(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "跟上时间(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(1, item)

        # self.gridLayoutWidget_3 = QtGui.QWidget(self.tab_3)
        # self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 811, 511))
        # self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        # self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        # self.gridLayout_3.setMargin(0)
        # self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("img/统计.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon8, _fromUtf8(""))


        """
        打开文件功能按钮设计
        """
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 90, 31, 23))
        self.pushButton_4.setToolTip(
            QtGui.QApplication.translate("MainWindow", "打开文件", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(
            QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("background:transparent")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("img/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QtCore.QSize(23, 23))

        """
        状态栏设计
        """
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.retranslateUi(MainWindow)

        """
        tab默认index选择
        """
        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1),
                                  QtGui.QApplication.translate("MainWindow", "心率", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QtGui.QApplication.translate("MainWindow", "轨迹", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QtGui.QApplication.translate("MainWindow", "统计", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.verticalHeaderItem(0)
        item = self.tableWidget.verticalHeaderItem(1)
        item = self.tableWidget.verticalHeaderItem(2)
        item = self.tableWidget.verticalHeaderItem(3)
        item = self.tableWidget.verticalHeaderItem(4)
        item = self.tableWidget.verticalHeaderItem(5)
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(1)