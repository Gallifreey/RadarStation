from core.hardware.Camera.CameraPlugin import CameraPlugin
from core.inference.AlertPlugin import AlertPlugin
from core.inference.YoloPlugin import YoloPlugin
from core.library.EasyImportBase import ROOT
from core.library.EventBase import EventBus, EventBusItemType
from core.library.Utils import Singleton

# TODO 场地模拟，创建虚拟场地，模拟算法结果
from radar_websocket.WebsocketPlugin import WebsocketPlugin


class Simulation(Singleton):
    """
    模拟类
    """

    def __init__(self):
        super().__init__()

    @classmethod
    def create_background(cls):
        """
        创建背景
        """
        pass

    @classmethod
    def read_config_file(cls):
        EventBus.read_config_file(ROOT("data/simulate_config.json"))

    @classmethod
    def start(cls):
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


Simulation.read_config_file()
Simulation.start()
