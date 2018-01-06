#-*- coding: utf-8 -*-
import cv2


def showImg(fileName):
    # 读取图像，支持 bmp、jpg、png、tiff 等常用格式
    img = cv2.imread(fileName)

    # 创建窗口
    cv2.namedWindow('Image')
    # 显示图像
    cv2.imshow('Image', img)
    # 显示窗口直到按下按键
    cv2.waitKey(0)
    #释放窗口
    cv2.destroyAllWindows()


showImg('./img/lu.jpg')