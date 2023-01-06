import cv2 as cv
import numpy as np

imgpath = "../../resource/chapter3/opencv-logo.png"
img = cv.imread(imgpath, cv.IMREAD_ANYDEPTH)  # 黑白加载
cv.imshow("image1", img)
cv.waitKey(0)

img = cv.imread(imgpath, cv.IMREAD_COLOR)  # 彩色加载
cv.imshow("image2", img)
cv.waitKey(0)

cv.destroyAllWindows()
