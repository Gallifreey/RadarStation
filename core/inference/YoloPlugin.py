import threading

import cv2
from numpy import random

from core.inference.yolov5.detect import YoloDetector
from core.library.EventBase import EventBus
from core.library.PluginBase import PluginBase


# TODO 精简化YOLO
class YoloPlugin(PluginBase):
    thread = None
    reproject_points = None  # 经反投影后的坐标
    annotator_result = None  # 检测结果图像
    armor_car_index = None  # armor-car索引表
    is_pause = False

    def __init__(self):
        super().__init__()
        self.plugin_name = 'yolo-plugin'
        self.priority = 1

    @classmethod
    def start(cls):
        thread = threading.Thread(target=cls.__yolo_thread, daemon=False)
        thread.start()

    @classmethod
    def uninstall(cls):
        cls.is_pause = True

    @classmethod
    def __yolo_thread(cls):
        YoloDetector.parent = cls
        while True:
            img = EventBus.get('camera_view')['data']
            if img is not None:
                YoloDetector.run(img)
