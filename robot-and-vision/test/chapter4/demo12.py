import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter4/1.jpg")
print(np.shape(img))
part = img[100:250, 50:150]
cv.imshow("origin", img)
cv.imshow("part", part)
cv.waitKey(0)
cv.destroyAllWindows()
