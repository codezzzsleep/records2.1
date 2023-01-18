import cv2 as cv

# 打开摄像头
image = cv.VideoCapture("../../resource/chapter13/test.avi")
# 图像宽度
print(image.set(3, 600))
image.set(cv.CAP_PROP_FRAME_WIDTH, 600)
# 图像高度
print(image.set(4, 500))
image.set(cv.CAP_PROP_FRAME_HEIGHT, 500)
# 视频帧率
image.set(5, 30)  # 设置帧率
image.set(cv.CAP_PROP_FPS, 30)
# 解码方式四字符
image.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('M', 'J', 'P', 'G'))
# 图像亮度
image.set(cv.CAP_PROP_BRIGHTNESS, 63)  # 设置亮度 -64 - 64  0.0
# 图像对比度
image.set(cv.CAP_PROP_CONTRAST, 0)  # 设置对比度 -64 - 64  2.0
# 图像曝光度
image.set(cv.CAP_PROP_EXPOSURE, 2000)  # 设置曝光值 1.0 - 5000  156.0

while image.isOpened():
    # 逐帧捕获
    ret, frame = image.read()
    # 显示图像
    cv.imshow("real_time", frame)
    # 等待按键ESC按下
    if cv.waitKey(5) == 27:
        break

# 释放摄像头
image.release()
# 关闭所有该程序打开的窗口
cv.destroyAllWindows()
