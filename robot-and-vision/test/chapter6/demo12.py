import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter6/1.jpg", 1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

dst = cv.equalizeHist(gray)
cv.imshow("dst", dst)
cv.waitKey()
