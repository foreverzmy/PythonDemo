import cv2


def putText(fileName, text, position, fontFamily, fontSize, color, fontWeight):
    """
    照片上添加文字

    Parameters
    ----------
    fileName : 文件名
    text : 添加的文字
    position : 左下角坐标
    fontFamily : 字体
    fontSize : 字号
    color : 颜色
    fontWeight : 字体粗细
    """
    img = cv2.imread(fileName)

    textImg = cv2.putText(img, text, position, fontFamily, fontSize, color,
                          fontWeight)

    cv2.namedWindow('putText')

    cv2.imshow('putText', textImg)

    # 显示窗口直到按下按键
    cv2.waitKey(0)
    #释放窗口
    cv2.destroyAllWindows()


putText('./img/lu.jpg', 'haha', (0, 20), cv2.FONT_HERSHEY_COMPLEX, 1,
        (128, 111, 278), 1)
