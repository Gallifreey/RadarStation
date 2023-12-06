import sys

import cv2

from core.hardware.Camera.CameraPlugin import CameraPlugin
from core.inference.AlertPlugin import AlertPlugin
from core.inference.YoloPlugin import YoloPlugin
from core.library.BehaviorTreeBase import BehaviorTree
from core.library.EasyImportBase import EasyImport
from core.library.EventBase import EventBus, EventBusItemType
from core.utils.logger import Logger
from radar_websocket.WebsocketPlugin import WebsocketPlugin


EventBus.read_config_file()
EventBus.install_plugin(CameraPlugin)
EventBus.install_plugin(YoloPlugin)
EventBus.install_plugin(AlertPlugin)
EventBus.install_plugin(WebsocketPlugin)
CameraPlugin.register(CameraPlugin.camera_view, 'camera_view', EventBusItemType.DATA)
YoloPlugin.register(YoloPlugin.reproject_points, 'reproject_points', EventBusItemType.DATA)
YoloPlugin.register(YoloPlugin.annotator_result, 'annotator_result', EventBusItemType.DATA)
YoloPlugin.register(YoloPlugin.armor_car_index, 'armor_car_index', EventBusItemType.DATA)
AlertPlugin.register(AlertPlugin.alert_msg, 'alert_msg', EventBusItemType.DATA)

EventBus.start()

# while True:
#     img = EventBus.get('annotator_result')['data']
#     if img is not None:
#         res = EventBus.get('armor_car_index')['data']
#         if res is not None:
#             for index, p in enumerate(res):
#                 row = int(index // 5)
#                 col = index % 5
#                 cv2.putText(img, 'No Target' if p[0] is None else str(p[0]), (col * 256 + 50, row * 256 + 50), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
#             cv2.imshow('output', img)
#             cv2.waitKey(1)


