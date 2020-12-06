# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import ctypes
import sys
from qt.QtSetupWindow import UiSetupForm


# from scripts.beeper import beep


class UiQtMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setup_window = None
        self.about_window = None
        self.manual_window = None
        self.stage_of_run = 0

        self.__initialization_off_all()

    def __initialization_off_all(self):
        self.__set_icon_in_taskbar_for_windows()
        self.__gui_initialization()
        self.__retranslate_ui()
        self.__move_main_window_to_initial_position()
        self.__set_all_bindings()
        self.__set_top_hint()

    @staticmethod
    def __set_icon_in_taskbar_for_windows() -> None:
        # Enable the app icon in the taskbar for windows
        # app_id = company.product.subproduct.version'  unicode arbitrary string
        app_id = u'Private.Viscometer.ComputerVisionDataCollector.beta'  # unicode arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    def __gui_initialization(self) -> None:

        self.setObjectName("QtMainWindow")
        self.setFixedSize(250, 300)
        self.setWindowIcon(QtGui.QIcon('images/analytics.png'))

        self.main_central_widget = QtWidgets.QWidget(self)
        self.main_central_widget.setObjectName("main_central_widget")

        self.dataTextEdit = QtWidgets.QTextEdit(self.main_central_widget)
        self.dataTextEdit.setGeometry(QtCore.QRect(10, 10, 230, 200))
        self.dataTextEdit.setReadOnly(True)
        self.dataTextEdit.setObjectName("dataTextEdit")
        self.dataTextEdit.setText("ready")

        self.nextPushButton = QtWidgets.QPushButton(self.main_central_widget)
        self.nextPushButton.setGeometry(QtCore.QRect(90, 220, 150, 28))
        self.nextPushButton.setObjectName("nextPushButton")

        self.runPushButton = QtWidgets.QPushButton(self.main_central_widget)
        self.runPushButton.setGeometry(QtCore.QRect(10, 220, 71, 28))
        self.runPushButton.setObjectName("runPushButton")
        self.runPushButton.setAutoFillBackground(True)

        self.setCentralWidget(self.main_central_widget)
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 250, 26))
        self.menu_bar.setObjectName("menu_bar")

        self.menuFile = QtWidgets.QMenu(self.menu_bar)
        self.menuFile.setObjectName("menuFile")

        self.menuInfo = QtWidgets.QMenu(self.menu_bar)
        self.menuInfo.setObjectName("menuInfo")
        self.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.setEnabled(True)
        self.status_bar.setSizeGripEnabled(False)
        self.status_bar.setObjectName("status_bar")
        self.setStatusBar(self.status_bar)

        self.actionRun = QtWidgets.QAction(self)
        icon_run = QtGui.QIcon()
        icon_run.addPixmap(QtGui.QPixmap("images/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon_run)
        self.actionRun.setObjectName("actionRun")

        self.actionAbort = QtWidgets.QAction(self)
        icon_abort = QtGui.QIcon()
        icon_abort.addPixmap(QtGui.QPixmap("images/abort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbort.setIcon(icon_abort)
        self.actionAbort.setObjectName("actionAbort")

        self.actionSetup = QtWidgets.QAction(self)
        icon_setup = QtGui.QIcon()
        icon_setup.addPixmap(QtGui.QPixmap("images/setup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSetup.setIcon(icon_setup)
        self.actionSetup.setObjectName("actionSetup")

        self.actionExit = QtWidgets.QAction("Quit", self)
        icon_exit = QtGui.QIcon()
        icon_exit.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon_exit)
        self.actionExit.setObjectName("actionExit")

        self.actionAbout = QtWidgets.QAction(self)
        icon_about = QtGui.QIcon()
        icon_about.addPixmap(QtGui.QPixmap("images/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon_about)
        self.actionAbout.setObjectName("actionAbout")

        self.actionManual = QtWidgets.QAction(self)
        icon_manual = QtGui.QIcon()
        icon_manual.addPixmap(QtGui.QPixmap("images/manual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManual.setIcon(icon_manual)
        self.actionManual.setObjectName("actionManual")

        self.menuFile.addAction(self.actionRun)
        self.menuFile.addAction(self.actionAbort)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSetup)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionAbout)
        self.menuInfo.addAction(self.actionManual)
        self.menu_bar.addAction(self.menuFile.menuAction())
        self.menu_bar.addAction(self.menuInfo.menuAction())

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def __retranslate_ui(self) -> None:
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("QtMainWindow", "VDA"))
        self.nextPushButton.setText(_translate("QtMainWindow", "Next->"))
        self.runPushButton.setText(_translate("QtMainWindow", "Run"))
        self.menuFile.setTitle(_translate("QtMainWindow", "File"))
        self.menuInfo.setTitle(_translate("QtMainWindow", "Info"))
        self.actionRun.setText(_translate("QtMainWindow", "Run"))
        self.actionRun.setShortcut(_translate("QtMainWindow", "Ctrl+R"))
        self.actionSetup.setText(_translate("QtMainWindow", "Setup"))
        self.actionSetup.setShortcut(_translate("QtMainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("QtMainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("QtMainWindow", "Ctrl+E"))
        self.actionAbout.setText(_translate("QtMainWindow", "About"))
        self.actionManual.setText(_translate("QtMainWindow", "Manual"))
        self.actionManual.setShortcut(_translate("QtMainWindow", "Ctrl+M"))
        self.actionAbort.setText(_translate("QtMainWindow", "Abort"))
        self.actionAbort.setShortcut(_translate("QtMainWindow", "Ctrl+A"))

    def __move_main_window_to_initial_position(self) -> None:
        self.__relocate_the_main_window()

    def __set_top_hint(self, state: bool = True) -> None:
        if state:
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)

    def __set_all_bindings(self):
        # self.actionRun.triggered.connect()
        # self.actionAbort.triggered.connect()
        self.actionSetup.triggered.connect(lambda: self.__open_setup())
        self.actionExit.triggered.connect(lambda: self.close())

        # self.actionAbout.triggered.connect()
        # self.actionManual.triggered.connect()

        # self.actionExit.triggered.connect()
        # self.runPushButton.clicked.connect()
        self.nextPushButton.clicked.connect(self.__test)

    def __relocate_the_main_window(self, x=None, y=None) -> None:
        if not (isinstance(x, (int, type(None)))
                and isinstance(y, (int, type(None)))
                and type(x) == type(y)):
            raise TypeError

        size = self.geometry()
        screen = QDesktopWidget().screenGeometry()

        if x is None:
            self.move((screen.width() - size.width()), 0)
        else:
            if y < 0:
                y = 0
            elif y + size.height() > screen.height():
                y = screen.height() - size.height()
            if x < 0:
                x = 0
            elif x + size.width() > screen.width():
                x = screen.width() - size.width()
            self.move(x, y)

    def closeEvent(self, event):
        if self.stage_of_run:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowIcon(QtGui.QIcon('images/analytics.png'))
            msg.setWindowTitle("Exit")
            msg.setText("Are you sure you want to exit the program?")
            msg.setInformativeText("The process is still running.")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            reply = msg.exec_()

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def __open_setup(self):
        if self.setup_window is None:
            self.setup_window = UiSetupForm()
            self.setup_window.setWindowModality(QtCore.Qt.ApplicationModal)
            self.setup_window.show()
        else:
            self.setup_window.setWindowModality(QtCore.Qt.ApplicationModal)
            self.setup_window.update_data()
            self.setup_window.show()

    @staticmethod
    def __test():
        print("test")


def run_qt_gui():
    app = QtWidgets.QApplication(sys.argv)
    main_window = UiQtMainWindow()
    main_window.show()
    sys.exit(app.exec_())
