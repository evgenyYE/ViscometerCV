import time
from PyQt5.QtCore import QThread, pyqtSignal
from scripts.find_on_screen import PatterFinderThread
from qt.QtTargetWindow import UiTargetForm
from scripts.beeper import beep
from datetime import datetime


class MainLogicProcess:

    def __init__(self, main_window):
        self.stage = 0
        self.target_window = UiTargetForm(self)
        self.main_window = main_window
        self.finder = PatterFinderThread()
        self.finder.signal.connect(self.blink)
        # self.finder.finished.connect(self.next)

    def if_running(self):
        if self.stage:
            return True
        else:
            return False

    def start(self):
        self.stage += 1
        self.finder.stage = self.stage

        self.finder.start()

    def stop(self):
        self.stage = 0
        if self.finder.isRunning():
            self.finder.stop()

    def restart(self):
        pass

    def reset(self):
        pass

    def blink(self, data):
        self.target_window.pull_target_window(offset=data[0], size=data[1])

    def next(self):
        self.stage += 1
        self.finder.stage = self.stage
        self.finder.start()

    def beep(self):
        pass

    def press(self):
        pass

    def write(self):
        pass

    def recognize_text(self):
        pass

    def recognize_image(self, stage):
        self.finder.stage = stage
        self.finder.stat()

    def write_to_excel(self):
        pass

    def relocate_do_directory(self):
        pass
