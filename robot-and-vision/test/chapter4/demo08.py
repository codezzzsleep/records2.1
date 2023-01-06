import cv2 as cv
import numpy as np

img = np.zeros((8, 8), dtype=np.uint8)
print("img=\n", img)
cv.imshow("one", img)
print("读取像素点img[0,3]", img[0, 3])
img[0, 3] = 255
print("修改后的像素 img[0,3]", img[0, 3])
print("img=\n", img)
cv.imshow("two", img)
cv.waitKey(0)
cv.destroyAllWindows()

