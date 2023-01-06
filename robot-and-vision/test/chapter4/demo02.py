import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter4/1.jpg")
arr = np.array(img)
cv.imshow("test", img)
cv.waitKey(2000)
for i in arr:
    for j in i:
        for k in j:
            print(k, end="")
            print(" ", end="")
        print()
