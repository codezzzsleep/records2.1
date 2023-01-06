import cv2 as cv
import numpy as np

img = np.zeros((300, 300, 3), dtype=np.uint8)
img[0:300, 0:300] = 255
cv.imshow("test.png", img)
cv.imwrite("../../resource/chapter5/module.png", img)
picture = cv.rectangle(img, (10, 10), (30, 40), (255, 0, 0), 2)
cv.imwrite("../../resource/chapter5/res.png", picture)
cv.imshow("res.png", picture)
cv.waitKey()
cv.destroyAllWindows()
