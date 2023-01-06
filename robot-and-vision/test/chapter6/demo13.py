import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter6/1.jpg", 1)
cv.imshow("origin", img)
b, g, r = cv.split(img)
bH = cv.equalizeHist(b)
gH = cv.equalizeHist(g)
rH = cv.equalizeHist(r)

result = cv.merge((bH, gH, rH))

cv.imshow("dst", result)
cv.waitKey()
