import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter6/1.jpg", 1)
imgYUV = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
cv.imshow("origin", img)
channelsYUV = list(cv.split(imgYUV))
channelsYUV[0] = cv.equalizeHist(channelsYUV[0])
channels = cv.merge(channelsYUV)
result = cv.cvtColor(channels, cv.COLOR_YCrCb2RGB)
cv.imshow("dst", result)
cv.waitKey()
