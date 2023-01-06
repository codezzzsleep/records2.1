import cv2 as cv
import numpy as np

a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print("np.round(2.4)", np.round(2.4))
print("np.round(a,1)", np.round(a, 1))
print("np.round(2.8)", np.round(2.8))
print("np.floor(2.5)", np.floor(2.5))
print("np.floor(2.6)", np.floor(2.6))
print("np.ceil(2.5)", np.ceil(2.5))
print("np.ceil(2.6)", np.ceil(2.6))
###############################################
# 输入结果
# np.round(2.4) 2.0
# np.round(a,1) [  1.    5.6 123.    0.6  25.5]
# np.round(2.8) 3.0
# np.floor(2.5) 2.0
# np.floor(2.6) 2.0
# np.ceil(2.5) 3.0
# np.ceil(2.6) 3.0
