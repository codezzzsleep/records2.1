import cv2 as cv
import numpy as np

img1 = cv.imread("../../resource/chapter4/1.jpg")
img2 = cv.imread("../../resource/chapter4/2.jpg")
cv.imshow("img1", img1)
cv.imshow("img2", img2)
part = img1[100:250, 50:150]
img2[100:250, 50:150] = part
cv.imshow("result", img2)
cv.waitKey()
cv.destroyAllWindows()
