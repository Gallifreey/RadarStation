import threading
import time

from core.library.PluginBase import PluginBase
from core.library.Utils import Singleton
from core.utils.logger import Logger
from radar_websocket.views import VideoStreamView, DataView, ReprojectView


class WebsocketPlugin(PluginBase, Singleton):

    def __init__(self):
        super().__init__()
        self.plugin_name = 'websocket_plugin'
        self.priority = 1

    @classmethod
    def start(cls):
        Logger.info('Websocket server starting...')
        thread = threading.Thread(target=cls.__web_thread, daemon=False)
        thread.start()
        Logger.info('Websocket server done.')

    @classmethod
    def uninstall(cls):
        pass

    @classmethod
    def __web_thread(cls):
        t = threading.Thread(target=cls.t1, daemon=False)
        t1 = threading.Thread(target=cls.t2, daemon=False)
        t2 = threading.Thread(target=cls.t3, daemon=False)
        t.start()
        time.sleep(1)
        t1.start()
        time.sleep(1)
        t2.start()

    @staticmethod
    def t1():
        view1 = VideoStreamView()

    @staticmethod
    def t2():
        view2 = DataView()

    @staticmethod
    def t3():
        view3 = ReprojectView()
