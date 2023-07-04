import cv2
import numpy as np
from torchvision.io import read_image
import torch
import torch.nn.functional as F
from os import listdir
from os.path import isfile, join
import cv2

mypath = "/home/youming/Desktop/osr/lwp/final/normal/"
onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

for fn in onlyfiles:
    if 'normal.png' in fn:
        img_pred = read_image('./val_level_1_fg_normal.png') / 255.
        # img_gt = read_image('./23-11_12_50_IMG_4927_normal.png') / 255.
        # img_gt = read_image('./01-09_14_00_IMG_0791_normal.png') / 255.
        # img_gt = read_image('./21-08_16_00_IMG_4592_normal.png') / 255.
        img_gt = read_image(fn) / 255.

        img_pred_normal = (img_pred) * 2 - 1
        torch.sum((img_pred_normal)**2, dim=0)

        img_gt_normal = img_gt * 2 - 1
        torch.sum((img_gt_normal)**2, dim=0)
        img_gt_normal = F.normalize(img_gt_normal, p=2, dim=0)

        # change coordinate should be added here!!
        img_gt_normal[2, :, :] = -img_gt_normal[2, :, :]
        img_tmp = img_gt_normal[1, :, :].clone()
        img_gt_normal[1, :, :] = img_gt_normal[0, :, :]
        img_gt_normal[0, :, :] = img_tmp

        img_gt_normal = (img_gt_normal + 1) / 2

        img = (255 * img_gt_normal.permute(1, 2, 0)).numpy()

        img = cv2.resize(img, (1280, 847), interpolation=cv2.INTER_AREA)
        # cv2.imwrite('./23-11_12_50_IMG_4927_normal_corrected.png', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        # cv2.imwrite('./01-09_14_00_IMG_0791_normal_corrected.png', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        # cv2.imwrite('./21-08_16_00_IMG_4592_normal_corrected.png', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        cv2.imwrite(fn.split('.png')[0] + '_correct.png', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))