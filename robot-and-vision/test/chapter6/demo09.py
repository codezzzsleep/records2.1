import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("../../resource/chapter6/1.jpg", 0)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
