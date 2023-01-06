import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter5/1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("origin", img)
cv.imshow("gray", gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey()
cv.destroyAllWindows()
