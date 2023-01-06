import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter5/module.png")
pointList = [(45, 45), (45, 45), (45, 32)]
sizeList = [(40, 25), (25, 11), (28, 11)]
color = (0, 0, 255)
cv.ellipse(img, pointList[0], sizeList[0], 0, 0, 360, color, 5, 8)
cv.ellipse(img, pointList[1], sizeList[1], 90, 0, 360, color, 5, 8)
cv.ellipse(img, pointList[2], sizeList[2], 0, 0, 360, color, 5, 8)
cv.imshow("丰田", img)
cv.waitKey()
cv.destroyAllWindows()
