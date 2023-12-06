import abc
import asyncio

import websockets


class RadarWebsocketViewBase(metaclass=abc.ABCMeta):

    def __init__(self):
        self.server = None
        self.host = '127.111.111.111'
        self.init()

    def init(self):
        """
        初始化ws，提供修改后的port及host构建url
        """
        # 重新获取事件循环
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        self.server = websockets.serve(self.enter, self.host, self.port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()

    @abc.abstractmethod
    async def enter(self, websocket):
        """
        websocket入口函数
        """
        pass
