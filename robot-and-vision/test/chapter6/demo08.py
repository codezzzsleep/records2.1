import copy

import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter6/1.jpg", 1)
grayImg = cv.imread("../../resource/chapter6/1.jpg", 0)

# cv.imshow("img", img)
# cv.imshow("gray", grayImg)
# cv.waitKey()
grayImg1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", grayImg)
# cv.imshow("gray1", grayImg1)
# cv.waitKey()
# print(grayImg == grayImg1)
# 事实证明，使用imread打开方式的灰度图和使用cvtColor去转换，内容是一样的
gamma = copy.deepcopy(grayImg1)
rows = img.shape[0]
clos = img.shape[1]
for i in range(rows):
    for j in range(clos):
        gamma[i][j] = 3 * pow(gamma[i, j], 0.8)
cv.imshow("img", img)
cv.imshow("gray", grayImg)
cv.imshow("gamma", gamma)
cv.waitKey()
