import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = cv.imread("../../resource/chapter6/1.jpg")


def showing(img, isgray=False):
    plt.axis("off")
    if isgray:
        plt.imshow(img, cmap="gray")
    else:
        plt.imshow(img)
    plt.show()


img = cv.imread("../../resource/chapter6/1.jpg")
img = np.array(img, dtype=np.int32)
img[..., 0] = img[..., 0] * 28.0
img[..., 1] = img[..., 1] * 151.0
img[..., 2] = img[..., 2] * 77.0
img = np.sum(img, axis=2)

arr = [np.right_shift(y.item(), 8) for x in img for y in x]
arr = np.array(arr)
arr.resize(img.shape)
showing(Image.fromarray(arr), True)
