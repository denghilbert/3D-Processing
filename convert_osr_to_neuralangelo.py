import numpy as np
import json
from argparse import ArgumentParser
import os
import cv2
from PIL import Image, ImageFile
from glob import glob
import math
import sys
from pathlib import Path

scene_list = os.listdir('./rgb')

f = open('./kai_cameras_normalized.json')
source_json = json.load(f)

out = {
        "k1": 0.0,  # take undistorted images only
        "k2": 0.0,
        "k3": 0.0,
        "k4": 0.0,
        "p1": 0.0,
        "p2": 0.0,
        "is_fisheye": False,
        "frames": []
}

for img_name in source_json.keys():
    camera_param = source_json[img_name]
    intrinsic_param = np.array(camera_param['K']).reshape(4, 4)
    w2c = np.array(camera_param['W2C']).reshape(4, 4)
    c2w = np.linalg.inv(w2c)
    frame = {"file_path": 'rgb/' + img_name, "transform_matrix": c2w.tolist()}
    out["frames"].append(frame)

fl_x = intrinsic_param[0][0]
fl_y = intrinsic_param[1][1]
cx = intrinsic_param[0][2]
cy = intrinsic_param[1][2]
sk_x = intrinsic_param[0][1]
sk_y = intrinsic_param[1][0]
w, h = camera_param['img_size'][0], camera_param['img_size'][1]

angle_x = math.atan(w / (fl_x * 2)) * 2
angle_y = math.atan(h / (fl_y * 2)) * 2

# scale_mat = scale_mat.astype(float)

out.update({
    "camera_angle_x": angle_x,
    "camera_angle_y": angle_y,
    "fl_x": fl_x,
    "fl_y": fl_y,
    "cx": cx,
    "cy": cy,
    "sk_x": sk_x,
    "sk_y": sk_y,
    "w": int(w),
    "h": int(h),
    "aabb_scale": 1.,
    "sphere_center": [0., 0., 0.],
    "sphere_radius": 1.,
})

file_path = os.path.join('./transforms.json')
with open(file_path, "w") as outputfile:
    json.dump(out, outputfile, indent=2)
print('Writing data to json file: ', file_path)

