# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from scripts.path import the_local_path


class UiAboutForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("AboutForm")
        self.setFixedSize(359, 276)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/analytics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 341, 261))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):

        html = self.__load_html()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AboutForm", "About"))
        self.textEdit.setHtml(_translate("AboutForm", html))

    @staticmethod
    def __load_html():
        try:
            path = the_local_path() + "/qt/About.html"
            with open(path, 'r') as f:
                html = f.read()
        except FileNotFoundError:
            html = 'File About.html not found'
        return html



