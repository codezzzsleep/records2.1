import cv2 as cv
import numpy as np

img = np.zeros((100, 200))
cv.imshow("windowname",img)
cv.waitKey(0)
cv.imshow("windowName2",img)
cv.waitKey(5000)
cv.destroyAllWindows()

