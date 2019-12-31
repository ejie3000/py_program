# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\3d\Desktop\test\UI\细节图提醒.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget
class Ui_xijie_tishi(object):
    def setupUi(self, xijie_tishi):
        xijie_tishi.setObjectName("xijie_tishi")
        xijie_tishi.resize(131, 63)
        self.xijie_tishi_label = QtWidgets.QLabel(xijie_tishi)
        self.xijie_tishi_label.setGeometry(QtCore.QRect(40, 10, 51, 41))
        self.xijie_tishi_label.setObjectName("xijie_tishi_label")

        self.retranslateUi(xijie_tishi)
        QtCore.QMetaObject.connectSlotsByName(xijie_tishi)

    def retranslateUi(self, xijie_tishi):
        _translate = QtCore.QCoreApplication.translate
        xijie_tishi.setWindowTitle(_translate("xijie_tishi", "细节图下载工具"))
        self.xijie_tishi_label.setText(_translate("xijie_tishi", "下载成功"))

if __name__ == '__main__':

    app = QApplication([])

    window1 = QWidget()

    ui1 = Ui_xijie_tishi()

    ui1.setupUi(window1)

    #ui.xijietu_Button.clicked.connect(on_click)

    window1.show()

    app.exec()