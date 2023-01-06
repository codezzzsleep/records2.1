import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[256, 256, 3], dtype=np.uint8)
cv.imshow("demo", img)
cv.waitKey(0)
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            img.itemset((i, j, k), 255)
cv.imshow("after", img)
cv.waitKey(0)
cv.destroyAllWindows()
