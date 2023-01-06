import cv2 as cv
import numpy as np


def opencv_muti_pic():
    img1 = cv.imread("../../resource/chapter3/1.jpg")
    print(np.shape(img1))
    img2 = cv.imread("../../resource/chapter3/2.jpg")
    print(np.shape(img2))
    img3 = cv.imread("../../resource/chapter3/3.jpg")
    print(np.shape(img3))
    imgs = np.hstack([img1, img2, img3])
    cv.imshow("mutil_pic", imgs)
    cv.waitKey(0)


opencv_muti_pic()
