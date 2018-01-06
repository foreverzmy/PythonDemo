import cv2


def readProperty(fileName):
    """
    读取图片的属性

    Parameters
    ----------
    fileName : 图片文件名
    """
    img = cv2.imread(fileName)
    print(img.shape)
    print(img.size)
    print(img.dtype)


readProperty('./img/worf.jpg')
readProperty('./img/gray.png')
readProperty('./img/create.png')
