import cv2 as cv
import numpy as np
import sys
alpha = 0.5
print("线性混合")
content = float(input('* 请输入第一幅图片的权重 alpha [0.0-1.0]:'))
print(content)
if 0 <= content <= 1:
    alpha = content
src1 = cv.imread("../../resource/chapter2/p1.jpg")
src2 = cv.imdecode(np.fromfile("../../resource/chapter2/山水.jpg", dtype=np.uint8), -1)
if src1 is None:
    sys.exit("Could not read the p1.png")
if src2 is None:
    sys.exit("Could not read the 山水.png")
beta = (1.0-alpha)
dst = cv.addWeighted(src1, alpha, src2, beta, 0.0, 0)
cv.imshow("result", dst)
cv.waitKey(0)

