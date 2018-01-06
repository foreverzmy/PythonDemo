# -*- coding: utf-8 -*-
import cv2
import numpy as np

"""
=== 思路 ===
核心: 将手机投影到电脑上，截取图像并处理

识别圆: 用 opencv 的 HoughCircles 方法找出图片中所有的圆和圆心
找出切点: 直接找出切点会有点繁琐，所以可以直接在两个圆心间划线，然后根据半径计算出交点也可以，或者直接等到飞机触碰到线时点击触发点击
识别飞机：根据颜色识别，准确率有待考证；
         通过图片识别，准确率有待考证
跳跃：通过 adb 直接触发点击事件，比通过操作屏幕点击更加快速
"""

img = cv2.imread('./01.png')

dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

gray = cv2.cvtColor(dst, cv2.COLOR_RGB2GRAY)  # 灰度图像

# hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
# lower_color = np.array([49, 28, 59])
# upper_color = np.array([58, 33, 70])
# mask = cv2.inRange(hsv, lower_color, upper_color)
# res = cv2.bitwise_and(dst, dst, mask=mask)

circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100)

cle = circle[0, :, :]

cle = np.uint16(np.around(cle))

for i in cle[:]:
    cv2.circle(dst, (i[0], i[1]), i[2], (0, 0, 255), 5)  # 画圆
    cv2.circle(dst, (i[0], i[1]), 2, (255, 0, 255), 10)  # 画圆心

cv2.namedWindow('WeGoing')
cv2.imshow('WeGoing', dst)
cv2.waitKey(0)
cv2.destroyWindow()
