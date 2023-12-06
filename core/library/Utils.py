import json
import threading
import cv2
import numpy as np


class Singleton(object):
    """
    单例类
    """
    _instance_lock = threading.Lock()

    def __init__(self, cls=None):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


# class CameraCalibrationUtils(Singleton):
#     """
#     相机标定工具类
#     """
#     board_w = 10 - 1
#     board_h = 7 - 1
#     from core.library.EasyImportBase import ROOT
#     config_file_path = ROOT('data/config.json')
#
#     def __init__(self):
#         super().__init__()
#
#     @classmethod
#     def start_calibrate(cls, video_source, saved_path):
#         frame = 0
#         frame_list = []
#         cap = cv2.VideoCapture(video_source)
#         while True:
#             ret, img = cap.read()
#             if ret:
#                 cv2.imshow("calibration_window", img)
#                 frame_list.append(img)
#                 if cv2.waitKey(30) & 0xFF == 27:
#                     break
#                 if cv2.waitKey(30) & 0xFF == 32:
#                     cv2.imwrite(f'{saved_path}/frame{frame}.jpg', img)
#         criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#         objp = np.zeros((cls.board_w * cls.board_h, 3), np.float32)
#         objp[:, :2] = np.mgrid[0:cls.board_w, 0:cls.board_h].T.reshape(-1, 2)
#         objp *= 18.1  # 18.1 mm
#         obj_points = []  # 在世界坐标系中的三维点
#         img_points = []  # 在图像平面的二维点
#         for index, image in enumerate(frame_list):
#             gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#             ret, corners = cv2.findChessboardCorners(gray, (cls.board_w, cls.board_h), None)
#             if ret:
#                 cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
#                 obj_points.append(objp)
#                 img_points.append(corners)
#                 cv2.drawChessboardCorners(image, (cls.board_w, cls.board_h), corners, ret)
#                 cv2.imshow("calibration_result", image)
#                 cv2.waitKey(1)
#         ret, mtx, dist, _, _ = \
#             cv2.calibrateCamera(obj_points, img_points, img.shape[::-1], None, None)
#         with open(cls.config_file_path, 'w') as f:
#             raw_data = json.load(f)
#             raw_data['camera_params'] = {
#                 'mtx': mtx,
#                 'dist': dist
#             }
#             json.dump(f, raw_data)
#             f.close()
#
#     @classmethod
#     def get_rt_mat(cls, truth_points):
#         from core.library.EventBase import EventBus
#         map_points, mtx, dist = EventBus.get('map_points'), EventBus.get('mtx'), EventBus.get('dist')
#         ref, r_vec, t_vec = cv2.solvePnP(map_points, truth_points, mtx, dist, flags=cv2.SOLVEPNP_ITERATIVE)
#         r_vec = cv2.Rodrigues(r_vec)[0]
#         t_vec = -np.matrix(r_vec).T * np.matrix(t_vec)
#         return r_vec, t_vec


class CameraLidarFusionCalibrationUtils(Singleton):
    """
    相机雷达融合标定工具类
    """
    pass
