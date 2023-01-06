import cv2 as cv
import numpy as np

img = cv.imread("../../resource/chapter8/opencv-logo.png")


def rotate_bond(img, angle):
    h, w, _ = img.shape
    cX, cY = w // 2, h // 2

    M = cv.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    res = cv.warpAffine(img, M, (nW, nH))
    cv.imshow("origin", img)
    cv.imshow("res", res)
    cv.waitKey()


rotate_bond(img, 45)
