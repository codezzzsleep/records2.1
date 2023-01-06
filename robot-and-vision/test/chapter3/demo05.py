import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter3/opencv-logo.png")
cv.namedWindow("myimg", cv.WINDOW_AUTOSIZE)
cv.namedWindow("my_image", cv.WINDOW_AUTOSIZE)
cv.imshow("myimg", img)
cv.waitKey(5000)


# 通过窗口标题来定位？