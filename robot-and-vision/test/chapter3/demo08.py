import cv2 as cv
import numpy as np

srcImage = [1]
width = 240
height = 120
szName = ("../../resource/chapter3/%d.jpg") % 1
srcImage[0] = cv.imread(szName)
cv.namedWindow(szName, cv.WINDOW_NORMAL)
cv.imshow(szName, srcImage[0])
cv.resizeWindow(szName, width, height)
cv.waitKey(0)
