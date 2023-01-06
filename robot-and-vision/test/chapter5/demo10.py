import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter5/contur.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contur, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contur, -1, (0, 0, 255), 3)
cv.imshow("img", img)
cv.waitKey()
