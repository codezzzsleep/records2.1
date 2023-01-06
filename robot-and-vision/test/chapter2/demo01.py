import cv2 as cv
img = cv.imread("../../resource/chapter2/opencv-logo.png")
cv.imshow("Hello, python opencv", img)
cv.waitKey(0)
cv.destoryAllWindows()