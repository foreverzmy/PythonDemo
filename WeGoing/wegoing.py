# -*- coding: utf-8 -*-
from cv2 import cv2
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


def getImg(fileName):
    """
    读取图片并将图片缩放为 1000 的宽度
    """
    img = cv2.imread(fileName)
    width = img.shape[:1][0]
    times = 1000 / width
    dst = cv2.resize(img, None, fx=times, fy=times,
                     interpolation=cv2.INTER_CUBIC)
    return dst


def getCircles(dst):
    gray = cv2.cvtColor(dst, cv2.COLOR_RGB2GRAY)  # 灰度图像
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100)

    cles = circles[0, :, :]
    cles = np.around(np.around(cles))  # 四舍五入，减少计算量
    return cles


def drawCircles(img, cles):
    for i in cles[:]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 5)  # 画圆
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 10)  # 画圆心
    return img


def showImg(img):
    cv2.namedWindow('WeGoing')
    cv2.imshow('WeGoing', img)
    cv2.waitKey(0)
    cv2.destroyWindow('WeGoing')


def main():
    dst = getImg('./02.png')  # 获取目标图像

    circles = getCircles(dst)
    dst = drawCircles(dst, circles)

    showImg(dst)


main()
