import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter6/1.jpg", 0)
height, width = img.shape[:2]
out = np.zeros(img.shape, np.uint8)
for i in range(height):
    for j in range(width):
        pix = img[i][j]
        if pix > 50:
            out[i][j] = 0.5 * pix
        elif pix < 150:
            out[i][j] = 3.6 * pix - 310
        else:
            out[i][j] = 0.238 * pix + 194
# out = out.around()
out = np.around(out)
out = out.astype(np.uint8)
cv.imshow("img", img)
cv.imshow("out",out)
cv.waitKey()
