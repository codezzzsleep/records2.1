import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter6/1.jpg")
height = np.shape(img)[0]
width = np.shape(img)[1]
graying = np.zeros((height, width, 3), np.uint8)
for i in range(height):
    for j in range(width):
        graying[i, j] = 0.3 * img[i, j][0] + 0.59 * img[i, j][1] + 0.11 * img[i, j][2]
cv.imshow("origin", img)
cv.imshow("graying", graying)
cv.waitKey()
cv.destroyAllWindows()

print(np.shape(img))
print(img.shape)

