import cv2
import numpy as np


def createEmptyImg(fileName):
    """
    创建形状相同的空白图像并保存
    
    Parameters
    ----------
    fileName : 图片文件名
    """
    img = cv2.imread(fileName)
    emptyImg = np.zeros(img.shape, np.uint8)
    cv2.imwrite('./img/create.png', emptyImg)


def copyImg(fileName):
    """
    拷贝图片并保存
    
    Parameters
    ----------
    fileName : 图片文件名
    """
    img = cv2.imread(fileName)
    copyImg = img.copy()
    cv2.imwrite('./img/copy.png', copyImg)


def turnGray(fileName):
    """
    将图片灰化并保存
    
    Parameters
    ----------
    fileName : 图片文件名
    """
    img = cv2.imread(fileName)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./img/gray.png', grayImg)


createEmptyImg('./img/worf.jpg')
copyImg('./img/worf.jpg')
turnGray('./img/worf.jpg')