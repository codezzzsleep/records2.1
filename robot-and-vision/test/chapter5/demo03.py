import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter5/module.png")
pointSize = 10
pointColor = (0, 0, 255)
# thickness 画图形用什么线条
thickness = -1

pointList = [(16, 16), (35, 40)]
for point in pointList:
    cv.circle(img, point, pointSize, pointColor, thickness)
    thickness = 4
cv.circle(img, (60, 60), 60, pointColor, 0)

cv.namedWindow("image")
cv.imshow("image", img)
cv.waitKey()
cv.destroyAllWindows()
