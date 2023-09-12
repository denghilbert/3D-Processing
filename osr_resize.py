from os import listdir
from os.path import isfile, join
import cv2

mypath = "/Users/youmingdeng/Downloads/rgb/"
onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

std_size = (1280, 845)
for fn in onlyfiles:
    img = cv2.imread(fn)
    print(img.shape, end=" ")
    resized = cv2.resize(img, std_size, interpolation = cv2.INTER_AREA)
    cv2.imwrite(fn, resized)
    print(resized.shape)

