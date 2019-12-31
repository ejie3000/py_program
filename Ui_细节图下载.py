# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\3d\Desktop\test\UI\细节图下载.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_xijietu(object):
    def setupUi(self, xijietu):
        xijietu.setObjectName("xijietu")
        xijietu.resize(292, 111)
        self.xijietu_Button = QtWidgets.QPushButton(xijietu)
        self.xijietu_Button.setGeometry(QtCore.QRect(100, 70, 75, 31))
        self.xijietu_Button.setObjectName("xijietu_Button")
        self.xijietu_label = QtWidgets.QLabel(xijietu)
        self.xijietu_label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.xijietu_label.setObjectName("xijietu_label")
        self.xijietu_lineEdit = QtWidgets.QLineEdit(xijietu)
        self.xijietu_lineEdit.setGeometry(QtCore.QRect(10, 29, 271, 31))
        self.xijietu_lineEdit.setObjectName("xijietu_lineEdit")

        self.retranslateUi(xijietu)
        QtCore.QMetaObject.connectSlotsByName(xijietu)

    def retranslateUi(self, xijietu):
        _translate = QtCore.QCoreApplication.translate
        xijietu.setWindowTitle(_translate("xijietu", "细节图下载工具"))
        self.xijietu_Button.setText(_translate("xijietu", "下  载"))
        self.xijietu_label.setText(_translate("xijietu", "输入官网商品链接："))
