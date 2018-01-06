import cv2
import numpy as np


def translate(fileName):
    """
    图像位移
    
    Parameters
    ----------
    fileName : 图片文件名
    """
    img = cv2.imread(fileName)
    rows, cols, *_ = img.shape

    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def scale(fileName):
    """
    图片缩放

    Parameters
    ----------
    fileName : 图片文件名
    """
    img = cv2.imread(fileName)
    res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # or
    # height, width = img.shape[:2]
    # res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

    cv2.imshow('img', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotate(fileName, degree):
    """
    图像旋转

    Parameters
    ----------
    fileName : 图片文件名
    """
    img = cv2.imread(fileName)
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), degree, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def affine(fileName):
    """
    仿射变换

    Parameters
    ----------
    fileName : 图片文件名
    """
    img = cv2.imread(fileName)
    rows, cols = img.shape[:2]

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1, pts2)

    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('image', dst)
    cv2.waitKey(0)


# translate('./img/worf.jpg')
# scale('./img/worf.jpg')
# rotate('./img/worf.jpg', 50)
affine('./img/worf.jpg')