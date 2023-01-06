import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter8/opencv-logo.png")

rows, cols, _ = img.shape

M = cv.getRotationMatrix2D((cols/2, rows/2), 360, 2)

res = cv.warpAffine(img, M, (2 * cols, 2 * rows))
# while (True):
cv.imshow("origin", img)
cv.imshow("result", res)
print(cv.waitKey())
cv.destroyAllWindows()
