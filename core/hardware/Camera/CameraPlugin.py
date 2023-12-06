from core.hardware.Camera.SingleCamera import SingleCamera
from core.library.PluginBase import PluginBase
from core.utils.logger import Logger


class CameraPlugin(PluginBase):
    __camera = SingleCamera()
    camera_view = None  # 摄像头视野

    def __init__(self):
        super().__init__()
        self.plugin_name = 'camera'
        self.priority = 1

    @classmethod
    def start(cls):
        cls.__camera.parent = cls
        cls.__camera.open()
        Logger.info(f'Camera open. Source from [VIDEO]')

    @classmethod
    def uninstall(cls):
        cls.__camera.close()
