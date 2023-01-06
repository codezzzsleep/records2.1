import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter8/opencv-logo.png")
rows, cols, channels = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
# 向下平移50，向右平移100

res = cv.warpAffine(img, M, (rows, cols))

cv.imshow("img", res)
cv.imwrite("../../resource/chapter8/warpAffine.png", res)
cv.waitKey()
cv.destroyAllWindows()
