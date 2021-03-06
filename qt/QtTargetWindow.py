# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'target.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDesktopWidget
import time
from datetime import datetime

class _WindBlinkerThread(QThread):
    signal = pyqtSignal(bool)
    INTERVAL = 0.2

    def run(self):
        for i in range(3):
            time.sleep(self.INTERVAL)
            self.signal.emit(False)
            time.sleep(self.INTERVAL)
            self.signal.emit(True)
        time.sleep(self.INTERVAL)

        self.signal.emit(False)


class UiTargetForm(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.__prepare_thread()
        self.setObjectName("Form")

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
        self.setWindowFlags(flags)

        self.resize(60, 30)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
        self.setWindowOpacity(0.6)
        self.setAutoFillBackground(False)

        self.__retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    @staticmethod
    def __retranslate_ui():
        _translate = QtCore.QCoreApplication.translate

    def __prepare_thread(self):
        self.blinker_thread = _WindBlinkerThread()
        self.blinker_thread.signal.connect(self.__blinker)
        self.blinker_thread.finished.connect(self.parent.next)

    def __blinker(self, state: bool):
        if state:
            self.show()
        else:
            self.hide()

    def pull_target_window(self, offset: tuple = (0, 0), size: tuple = (60, 30)) -> None:
        self.__relocate_win(offset)
        self.__resize_win(size)
        self.blinker_thread.start()

    def __resize_win(self, size) -> None:
        self.resize(size[0], size[1])

    def __relocate_win(self, offset) -> None:
        x = offset[0]
        y = offset[1]
        if not (isinstance(x, (int, type(None)))
                and isinstance(y, (int, type(None)))
                and type(x) == type(y)):
            raise TypeError
        self.move(x, y)
