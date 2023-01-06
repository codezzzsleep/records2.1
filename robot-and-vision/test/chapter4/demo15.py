import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter4/1.jpg")
b, g, r = cv.split(img)
bgr = cv.merge([b, g, r])
rgb = cv.merge([r, g, b])
grb = cv.merge((g, r, b))
cv.imshow("bgr", bgr)
cv.imshow("rgb", rgb)
cv.imshow("grb", grb)
cv.waitKey()
cv.destroyAllWindows()
