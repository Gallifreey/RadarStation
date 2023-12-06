from core.library.LidarBase import Lidar


class LivoxMid70(Lidar):
    """
    此为Livox Mid 70雷达类，用于创建、管理雷达，并通信。
    """
    def __init__(self):
        super().__init__()

    def build_connection(self, path):
        pass

    def start(self):
        pass

    def close(self):
        pass

    def callback(self, data):
        pass
