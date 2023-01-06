import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
for i in range(512):
    for j in range(512):
        img[i, j, :] = [i % 256, j % 256, (i + j) % 256]
info = "Hello world"
fontFace = cv.FONT_HERSHEY_COMPLEX
fontScale = 2
thickness = 2
textSize = cv.getTextSize(info, fontFace, fontScale, thickness)
print(textSize)
printCenter = (int(521 / 2 - textSize[0][0] / 2), int(512 / 2 - textSize[0][1] / 2))
cv.putText(img, info, printCenter, fontFace, fontScale, (255, 255, 255), thickness)
cv.imshow("res", img)
cv.waitKey()
cv.destroyAllWindows()
