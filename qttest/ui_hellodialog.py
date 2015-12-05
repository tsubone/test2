# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hellodialog.ui'
#
# Created: Sat Dec  5 00:43:43 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_HelloDialog(object):
    def setupUi(self, HelloDialog):
        HelloDialog.setObjectName("HelloDialog")
        HelloDialog.resize(400, 300)
        self.lineEdit = QtGui.QLineEdit(HelloDialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 381, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtGui.QLabel(HelloDialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 381, 20))
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(HelloDialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 250, 98, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(HelloDialog)
        QtCore.QMetaObject.connectSlotsByName(HelloDialog)

    def retranslateUi(self, HelloDialog):
        HelloDialog.setWindowTitle(QtGui.QApplication.translate("HelloDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HelloDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("HelloDialog", "Hello", None, QtGui.QApplication.UnicodeUTF8))

