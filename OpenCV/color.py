# 实现识别视频中蓝色的部分
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()  # 读取视频的每一帧
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 将图片从 BGR 空间转到 HSV 空间

    # 定义在HSV空间中蓝色的范围
    lower_blue = cv2.cvtColor([], cv2.COLOR_BGR2HSV)
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # 根据以上定义的蓝色的阈值得到蓝色的部分

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
