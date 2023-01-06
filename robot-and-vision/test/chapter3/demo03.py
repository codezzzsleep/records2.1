import cv2 as cv
import numpy as np

img = cv.imread('../../resource/chapter3/opencv-logo.png')
print(np.shape(img))

height = np.shape(img)[0]
width = np.shape(img)[1]
channles = np.shape(img)[2]
print("height", height, "weight", width, "channles", channles)

height, width, channles = np.shape(img)[:3]
print("height", height, "weight", width, "channles", channles)
# 长度 宽度 通道数

