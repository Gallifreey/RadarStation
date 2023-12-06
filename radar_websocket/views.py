import asyncio
import time
import base64
import json
import random

import cv2
import numpy as np
import websockets

from core.library.EasyImportBase import ROOT
from core.library.EventBase import EventBus
from core.library.RadarWebsocketBase import RadarWebsocketViewBase


class VideoStreamView(RadarWebsocketViewBase):

    def __init__(self):
        self.port = 1000
        super().__init__()

    async def enter(self, websocket):
        while True:
            result, img_encode = cv2.imencode('.jpg', EventBus.get('annotator_result')['data'])
            data = np.array(img_encode)
            img = data.tobytes()
            img = base64.b64encode(img).decode()
            ws_buffer = {
                'img': "data:image/jpeg;base64," + img
            }
            await websocket.send(json.dumps(ws_buffer))


class DataView(RadarWebsocketViewBase):
    def __init__(self):
        self.port = 1001
        super().__init__()

    async def enter(self, websocket):
        with open(ROOT('data/config.json'), 'r') as f:
            data = f.readlines()
            await websocket.send(data)


class ReprojectView(RadarWebsocketViewBase):

    def __init__(self):
        self.port = 1002
        super().__init__()

    async def enter(self, websocket):
        while True:
            ws_buffer = {
                'robots': [
                    [0, [random.randint(0, 592), random.randint(0, 1107)]],
                    [0, [random.randint(0, 592), random.randint(0, 1107)]],
                    [1, [random.randint(0, 592), random.randint(0, 1107)]],
                    [0, [random.randint(0, 592), random.randint(0, 1107)]],
                    [1, [random.randint(0, 592), random.randint(0, 1107)]],
                    [1, [random.randint(0, 592), random.randint(0, 1107)]]
                ]
            }
            time.sleep(0.3)
            await websocket.send(json.dumps(ws_buffer))
