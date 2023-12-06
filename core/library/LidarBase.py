import abc


class Lidar(metaclass=abc.ABCMeta):
    info: dict

    def __init__(self):
        pass

    @abc.abstractmethod
    def build_connection(self, path):
        """
        用于向雷达ROS端建立连接 \n
        :param path: 雷达ROS Topic路径
        """
        pass

    @abc.abstractmethod
    def start(self):
        """
        开启雷达
        """
        pass

    @abc.abstractmethod
    def close(self):
        """
        关闭雷达
        """
        pass

    @abc.abstractmethod
    def callback(self, data):
        """
        雷达回调函数，用于轮询ROS Topic获取其雷达数据 \n
        :param data: 雷达数据
        """
        pass

    def main_loop(self):
        """
        主线程防阻塞
        """
        pass
