import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt


def main():
    img = cv.imread("../../resource/chapter6/1.jpg", 0)
    xy = xygray(img)

    x_rang = range(256)
    plt.plot(x_rang, xy, linewidth=2, c="black")
    y_maxValue = np.max(xy)
    plt.axis([0, 255, 0, y_maxValue])
    plt.xlabel("gray Level")
    plt.ylabel("number of pixels")
    plt.show()


def xygray(img):
    rows, cols = img.shape
    xy = np.zeros([256], np.uint64)
    for r in range(rows):
        for c in range(cols):
            xy[img[r][c]] += 1
    return xy


main()
