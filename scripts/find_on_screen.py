import cv2
import numpy as np
from PIL import ImageGrab
from scripts.timer import execution_time_plotter
from PIL import Image
from scripts.path import the_local_path
import time
from PyQt5.QtCore import QThread, pyqtSignal


class PatterFinderThread(QThread):
    signal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(PatterFinderThread, self).__init__(parent)
        self.thread_active = True
        self.stage = 1

    def run(self):
        self.thread_active = True
        result = [(0, 0), (60, 30)]
        while self.thread_active:
            result = find(self.stage)
            if result is not None:
                self.signal.emit(result)
                break

    def stop(self):
        self.thread_active = False
        self.wait()


def _image_path_by_stage(stage: int) -> str:
    file_names = ['1_job_editor.png',
                  '2_job_editor - save.png',
                  '3_identification.png',
                  '4_identification - ok.png',
                  '5_temperature_accept.png',
                  '6_place_sample.png',
                  '7_place_sample - ok.png',
                  '8_geometry.png',
                  '9_geometry - ok.png',
                  '10_measure.png',
                  '11_measure_ok.png',
                  '12-clean.png',
                  '13-clean - ok.png',
                  '14-save_pattern.png',
                  '15-save_pattern - text.png',
                  '16-save_pattern - save.png',
                  '14-save_pattern.png',
                  '15-save_pattern - text.png',
                  '16-save_pattern - save.png']
    return the_local_path() + '\\images\\patterns\\' + file_names[stage - 1]


# @execution_time_plotter
def find(stage: int):
    img_rgb = ImageGrab.grab().convert("RGB")
    img_rgb = np.array(img_rgb)
    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = Image.open(_image_path_by_stage(stage))
    template = np.array(template)
    template = cv2.cvtColor(template, cv2.COLOR_RGB2BGR)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.82  # make a automation for optimal threshold detection(!!!)

    location_array = np.where(res >= threshold)

    data = []
    for pt in zip(*location_array[::-1]):
        data.append(pt)

    if not len(data):
        return None

    x = 0
    y = 0
    for i in range(len(data)):
        x = data[i][0] + x
        y = data[i][1] + y

    x = int(x / len(data))
    y = int(y / len(data))

    pt = (x, y)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)  # this is only for test(!!!)

    cv2.imwrite('07_result_TM_CCOEFF_NORMED.png', img_rgb)  # this is only for test(!!!)

    return [(x, y), (w, h)]
