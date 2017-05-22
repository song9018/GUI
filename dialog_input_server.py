# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_input.ui'
#
# Created: Fri Apr 21 18:46:08 2017
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(310, 181)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 30, 181, 16))
        self.label.setText(QtGui.QApplication.translate("Form", "日期输入(0.01 10)：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 59, 171, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_dialog_server = QtGui.QPushButton(Form)
        self.pushButton_dialog_server.setGeometry(QtCore.QRect(60, 120, 75, 23))
        self.pushButton_dialog_server.setText(QtGui.QApplication.translate("Form", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_dialog_server.setObjectName(_fromUtf8("pushButton_dialog_server"))
        self.pushButton_dialog_server_2 = QtGui.QPushButton(Form)
        self.pushButton_dialog_server_2.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.pushButton_dialog_server_2.setText(QtGui.QApplication.translate("Form", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_dialog_server_2.setObjectName(_fromUtf8("pushButton_dialog_server_2"))
        self.pushButton_dialog_server_3 = QtGui.QPushButton(Form)
        self.pushButton_dialog_server_3.setGeometry(QtCore.QRect(280, 0, 31, 23))
        self.pushButton_dialog_server_3.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./img/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_dialog_server_3.setIcon(icon)
        self.pushButton_dialog_server_3.setIconSize(QtCore.QSize(31, 23))
        self.pushButton_dialog_server_3.setObjectName(_fromUtf8("pushButton_dialog_server_3"))
        self.pushButton_dialog_server_3.setStyleSheet("background:transparent")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

