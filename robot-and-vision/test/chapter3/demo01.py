import cv2 as cv
import numpy as np

imgpath = "../../resource/chapter3/opencv-logo.png"
img = cv.imdecode(np.fromfile(imgpath, dtype=np.uint8), -1)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
