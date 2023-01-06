import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter6/1.jpg", 0)
out = 2.0 * img

out[out > 255] = 255
out = np.around(out)
out = out.astype(np.uint8)
cv.imshow("img", img)
cv.imshow("out", out)
cv.waitKey()
