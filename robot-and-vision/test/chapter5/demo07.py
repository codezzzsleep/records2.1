import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter5/module.png")
Pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv.fillPoly(img, [Pts], (255, 0, 0))
cv.imshow("res", img)
cv.waitKey()
cv.destroyAllWindows()
