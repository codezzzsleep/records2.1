import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter3/opencv-logo.png")
height, width = np.shape(img)[:2]
cv.line(img, (0, 0), (width, height), (50, 50, 188), 2)
cv.imwrite("../../resource/chapter3/re_opencv-logo.png", img)
img = cv.imread("../../resource/chapter3/re_opencv-logo.png")
cv.imshow("image", img)
cv.waitKey(0)

cv.imshow("image_orgin", cv.imread("../../resource/chapter3/opencv-logo.png"))
cv.waitKey(0)

cv.destroyAllWindows()
