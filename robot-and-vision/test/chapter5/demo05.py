import cv2 as cv
import numpy as np

WINDOW_WIDTH = 200


def drawFilledCricle(img, center):
    thickness = -1
    lineType = 8
    color = (0, 0, 255)
    cv.circle(img, center, WINDOW_WIDTH // 32, color, thickness, lineType)


def drawEllipse(img, angle):
    thickness = 2
    lineType = 8
    color = (255, 129, 0)
    pt = (WINDOW_WIDTH // 2, WINDOW_WIDTH // 2)
    size = (WINDOW_WIDTH // 4, WINDOW_WIDTH // 16)
    cv.ellipse(img, pt, size, angle, 0, 360, color, thickness, lineType)


heigh = WINDOW_WIDTH
width = WINDOW_WIDTH
atomImage = np.zeros((heigh, width, 3), np.uint8)
rookImage = np.zeros((heigh, width, 2), np.uint8)
drawEllipse(atomImage, 90)
drawEllipse(atomImage, 0)
drawEllipse(atomImage, 45)
drawEllipse(atomImage, -45)
drawFilledCricle(atomImage, (WINDOW_WIDTH // 2, WINDOW_WIDTH // 2))
cv.imshow("result", atomImage)
cv.waitKey()
cv.destroyAllWindows()
