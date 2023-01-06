import cv2 as cv
import numpy as np

g_nTrackbarMaxValue = 9
g_nTrackbarValue = 0
g_nKernelValue = 0
g_srcImage = cv.imread("../../resource/chapter7/opencv-logo.png")
g_dstImage = cv.imread("../../resource/chapter7/opencv-logo.png")
windowName = "Mean filtering"


def on_kernelTrackbar(x):
    global g_nTrackbarValue
    g_nTrackbarValue = cv.getTrackbarPos("res", windowName)
    g_nKernelValue = g_nTrackbarValue * 2 + 1
    ksize = (g_nKernelValue, g_nKernelValue)
    cv.blur(g_srcImage, ksize, g_dstImage)


cv.namedWindow("src", cv.WINDOW_AUTOSIZE)
cv.imshow("src", g_srcImage)
cv.namedWindow(windowName)
cv.createTrackbar("res", windowName, 0, 9, on_kernelTrackbar)
while (True):
    cv.imshow(windowName, g_dstImage)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
