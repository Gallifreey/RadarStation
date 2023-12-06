import numpy as np
from typing import Tuple, Any

from core.library.EventBase import EventBus
from core.library.Utils import CameraCalibrationUtils


def fusion_distance_from_region(point_cloud):
    """
    点云距离融合 \n
    :param point_cloud: 切割后的点云
    :return: 融合的平均距离
    """
    w, h = EventBus.get('fusion_region_shape')
    distance = []
    for i in range(w):
        for j in range(h):
            distance.append(point_cloud[i][j])
    return float(np.array(distance).mean())


def xyd2xy(distance, camera_view_point):
    """
    :param distance: 雷达距离
    :param camera_view_point: 相机平面坐标
    :return: 小地图坐标
    """
    mtx, dist = EventBus.get('mtx'), EventBus.get('dist')
    r_vec, t_vec = CameraCalibrationUtils.get_rt_mat([])
    u, v = camera_view_point[0], camera_view_point[1]
    (xw, yw, zw, holder) = np.linalg.inv(r_vec) @ (distance * np.linalg.inv(mtx) @ np.matrix([u, v, 1]) - t_vec)
    return xw, yw, zw

