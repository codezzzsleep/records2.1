import cv2 as cv
import numpy as np


def fill_binary():
    img = np.zeros([400, 400, 3], np.uint8)
    img[0:200, 0:400, :] = 255
    cv.imshow("fill_binary", img)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[0:400, 101:301] = 0
    # img[199,199] = 255
    cv.floodFill(img, mask, (199, 199), (0, 183, 183), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", img)

fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()

