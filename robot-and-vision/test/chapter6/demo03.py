import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter6/1.jpg")
height = np.shape(img)[0]
width = np.shape(img)[1]

graying = np.zeros((height, width, 3), np.uint8)

for i in range(height):
    for j in range(width):
        # graying[i, j] = (img[i, j][0] + img[i, j][1] + img[i, j][2]) / 3
        graying[i, j] = (img[i, j][0] / 3 + img[i, j][1] / 3 + img[i, j][2] / 3)

cv.imshow("origin", img)
cv.imshow("graying", graying)
cv.waitKey()
cv.destroyAllWindows()
# RuntimeWarning: overflow encountered in ubyte_scalars
# graying[i, j] = (img[i, j][0] + img[i, j][1] + img[i, j][2]) / 3
# graying[i, j] = (img[i, j][0] / 3 + img[i, j][1] / 3 + img[i, j][2] / 3)
