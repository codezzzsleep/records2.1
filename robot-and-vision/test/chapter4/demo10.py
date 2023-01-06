import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[256, 256], dtype=np.uint8)
cv.imshow("随机灰度图", img)
print("img\n", img)
img = np.random.randint(0, 256, size=[256, 256], dtype=np.uint8)
cv.imshow("随机灰度图", img)
print("img\n", img)
cv.waitKey(0)
cv.destroyAllWindows()
