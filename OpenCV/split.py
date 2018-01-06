# 通道的拆分/合并处理
import cv2
import numpy as np

img = cv2.imread('./img/lu.jpg')
emptyImg = np.zeros(img.shape[:2], np.uint8)

# 通道分离，注意顺序BGR不是RGB
(b, g, r) = cv2.split(img)

cv2.imshow('imgb', b)
cv2.waitKey(0)
cv2.imshow('imgg', g)
cv2.waitKey(0)
cv2.imshow('imgr', r)
cv2.waitKey(0)
# 同道合并
imgb = cv2.merge([b, emptyImg, emptyImg])
imgg = cv2.merge([emptyImg, g, emptyImg])
imgr = cv2.merge([emptyImg, emptyImg, r])

cv2.imshow('imgb', imgb)
cv2.waitKey(0)
cv2.imshow('imgg', imgg)
cv2.waitKey(0)
cv2.imshow('imgr', imgr)
cv2.waitKey(0)

cv2.destroyAllWindows()