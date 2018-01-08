# -*- coding: utf-8 -*-
import os
import cv2
import time
import numpy as np
import win32api
from PIL import ImageGrab
"""
=== 思路 ===
核心: 将手机投影到电脑上，截取图像并处理

识别圆: 用 opencv 的 HoughCircles 方法找出图片中所有的圆和圆心
找出切点: 根据两个相切圆的圆心和半径找到交点
识别飞机：根据颜色识别，准确率有待考证；
         通过图片识别，准确率有待考证
跳跃：通过 adb 直接触发点击事件，比通过操作屏幕点击更加快速
"""


def get_img(a, b, c, d):
    """
    读取图片并将图片缩放为 1000 的宽度
    """
    img = ImageGrab.grab((a, b, c, d)).convert('RGB')
    img = np.asarray(img)
    # img = cv2.imread('./images/02.png')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # img = cv2.GaussianBlur(img, (5, 5), 1.5)
    width = img.shape[:1][0]
    times = 1000 / width
    dst = cv2.resize(img, None, fx=times, fy=times,
                     interpolation=cv2.INTER_CUBIC)
    return dst


def get_airplane(img):
    """
    获取飞机的坐标
    """
    w, h = img.shape[:2]
    pixel_x_sum = 0
    pixel_y_sum = 0
    pixel_count = 0
    for i in range(w):
        for j in range(h):
            pixel = img[i, j]
            if(15 < pixel[2] < 20 and 80 < pixel[1] < 90 and 110 < pixel[0] < 120):
                pixel_x_sum += j
                pixel_y_sum += i
                pixel_count += 1
    if all((pixel_x_sum, pixel_y_sum, pixel_count)):
        pixel_x = int(pixel_x_sum / pixel_count)
        pixel_y = int(pixel_y_sum / pixel_count)
    return pixel_x, pixel_y


def draw_airplane(img, point):
    """
    将飞机所在点在图上标出来
    """
    cv2.circle(img, (point[0], point[1]), 2, (0, 0, 255), 10)
    return img


def get_circles(dst):
    """
    获取图片上所有圆的圆心坐标与半径
    """
    gray = cv2.cvtColor(dst, cv2.COLOR_RGB2GRAY)  # 灰度图像
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100)
    large_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, circles=None,
                                     param1=100, param2=30, minRadius=100, maxRadius=300)
    cles = circles[0, :, :]
    # cles = large_circles[0, :, :]
    cles = np.around(np.around(cles))  # 四舍五入，减少计算量
    cles = cles[np.lexsort(-cles[:, :-1:].T)]
    return cles


def draw_circles(img, cles):
    """
    在图片上把圆画出来
    """
    for i in cles[:]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 5)  # 画圆
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 10)  # 画圆心
    return img


def get_tangency(cles, air):
    """
    获取相切圆的切点
    """
    point = []
    for idx, item in enumerate(cles):
        if(((item[0] - air[0])**2 + (item[1] - air[1])**2 < item[2]**2) and idx < len(cles)):
            a = item[:2]
            b = cles[idx + 1][:2]
            r1 = item[2]
            r2 = cles[idx + 1][2]
            px = b[0] - (r2 * (b[0] - a[0]) / (r1 + r2))
            py = b[1] - (r2 * (b[1] - a[1]) / (r1 + r2))
            point = [px, py]
            break
    point = np.around(point)
    return point


def draw_tangency(img, tangency):
    """
    将圆切点画在图像上
    """
    cv2.circle(img, tuple(tangency), 2, (255, 0, 0), 10)
    return img


def show_img(img):
    """
    显示图片
    """
    cv2.namedWindow('WeGoing')
    cv2.imshow('WeGoing', img)
    cv2.waitKey(0)
    cv2.destroyWindow('WeGoing')


def jump():
    cmd = 'adb shell input tap %s %s' % (800, 300)
    os.system(cmd)


def distance(air, tangency):
    """
    计算
    """
    if ((air[0] - tangency[0])**2 + (air[1] - tangency[1]) < 20**2):
        # jump()
        print('jump')
    else:
        print('next')


def main():
    """
    主函数
    """
    print('begin')
    dst = get_img(0, 200, 540, 1020)  # 获取目标图像
    time_start = time.time()
    # 飞机
    airplane = get_airplane(dst)
    # dst = draw_airplane(dst, airplane)
    # 圆
    circles = get_circles(dst)
    # dst = draw_circles(dst, circles)
    # 切点
    tangency = get_tangency(circles, airplane)
    if tangency.any():
        distance(airplane, tangency)
        # dst = draw_tangency(dst, tangency)
    else:
        print(False)

    # show_img(dst)
    time_end = time.time()
    print(time_end - time_start)
    main()
    # cv2.imwrite('./create.png', dst)


main()
