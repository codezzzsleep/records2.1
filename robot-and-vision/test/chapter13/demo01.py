import cv2 as cv
import numpy as np

video = cv.VideoCapture("../../resource/chapter13/sea.mp4")

fps = video.get(cv.CAP_PROP_FPS)
# size = (int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
# FNUMS = video.get(cv.CAP_PROP_FRAME_COUNT)
# print(size)
success, frame = video.read()

while success:
    cv.setWindowTitle("test", "this is test")
    # frame = cv.resize(frame, (720, 1280))
    print(video.set(3, 600))
    print(video.set(4, 600))
    cv.imshow("window", frame)
    cv.waitKey(int(1000 / int(fps)))
    success, frame = video.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
