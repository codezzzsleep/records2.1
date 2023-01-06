import cv2 as cv
import numpy as np

szName = ["", "", ""]
srcImage = [1, 2, 3]
for i in range(0, 2):
    szName[i] = ("../../resource/chapter3/%d.jpg") % (i + 1)
    srcImage[i] = cv.imread(szName[i])
    cv.imshow(szName[i], srcImage[i])
    cv.waitKey(3750)
    cv.imshow(szName[i],srcImage[i])
    cv.destroyWindow(szName[i])