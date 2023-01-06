import cv2 as cv
import numpy as np

img = np.zeros((200, 200))


def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 20, 255, -1)


cv.namedWindow('img')
cv.setMouseCallback('img', draw_circle)
while (1):
    cv.imshow('img', img)
    n = cv.waitKey(5)
    if n == ord('q'):
        break
    elif n == ord('s'):
        cv.imwrite("res.jpg", img)
        print("保存成功")
cv.destroyAllWindows()
