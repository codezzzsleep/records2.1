import cv2 as cv
import numpy as np

alpha = 0.3
beta = 80
imgpath = "../../resource/chapter3/1.jpg"
img1 = cv.imread(imgpath)
img2 = cv.imread(imgpath)


def updateAlpah(x):
    global alpha, img1, img2
    alpha = cv.getTrackbarPos("alpha", "image")
    alpha = alpha * 0.01
    img1 = np.uint8(np.clip((alpha * img2 + beta), 0, 255))


def updateBeta(x):
    global beta, img1, img2
    beta = cv.getTrackbarPos("beta", "image")
    img1 = np.uint8(np.clip((alpha * img2 + beta), 0, 255))


cv.namedWindow("image")
cv.createTrackbar("alpha", "image", 0, 300, updateAlpah)
cv.createTrackbar("beta", "image", 0, 255, updateBeta)

while (1):
    cv.imshow("image", img1)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
