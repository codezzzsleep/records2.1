import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter4/1.jpg")
cv.imshow("origin", img)
blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]
cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)
_blue = img
_blue[:, :, 0] = 0
_green = img
_green[:, :, 1] = 0
_red = img
_red[:, :, 2] = 0
# cv.imshow("_blue", _blue)
# cv.imshow("_green", _green)
# cv.imshow("_red", _red)

img = cv.imread("../../resource/chapter4/1.jpg")
blue = cv.split(img)[0]
green = cv.split(img)[1]
red = cv.split(img)[2]
cv.imshow("blue1", blue)
cv.imshow("green1", green)
cv.imshow("red1", red)
cv.waitKey()
cv.destroyAllWindows()
