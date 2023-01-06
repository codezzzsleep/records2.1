import cv2 as cv
import numpy as np
import math


def logTransform(c, img):
    # height, width, deep = img.shape[:3]
    # newImg = np.zeros(img.shape)
    # for i in range(height):
    #     for j in range(width):
    #         for k in range(deep):
    #             newImg[i, j, k] = c * (math.log(1.0 + img[i, j, k]))
    height, width = img.shape[:2]
    newImg = np.zeros(img.shape)
    for i in range(height):
        for j in range(width):
            newImg[i, j] = c * (math.log(1.0 + img[i, j]))
    newImg = cv.normalize(newImg, newImg, 0, 255, cv.NORM_MINMAX)
    return newImg


img = cv.imread("../../resource/chapter6/1.jpg", 0)
logImg = logTransform(1.0, img)
cv.imshow("logImg", logImg)
cv.imwrite("../../resource/chapter6/logImg.png", logImg)
cv.waitKey()
