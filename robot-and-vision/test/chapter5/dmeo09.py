import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter5/module.png")
cv.imshow("origin", img)

replicate = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REPLICATE)
cv.imshow("BORDER_REPLICATE", replicate)
replicate = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_CONSTANT)
cv.imshow("BORDER_CONSTANT", replicate)
replicate = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REFLECT)
cv.imshow("BORDER_REFLECT", replicate)
replicate = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REFLECT101)
cv.imshow("BORDER_REFLECT101", replicate)
replicate = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_WRAP)
cv.imshow("BORDER_WRAP", replicate)
cv.waitKey()