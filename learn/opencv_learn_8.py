import cv2
import numpy as np
import random

# opencv_learn_7 为自己写的阈值分割算法 可通过调整滑动条来改变阈值分割效果
# 这个文件来使用cv库中提供的阈值分割函数做阈值分割

path = "./pic/3.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (640, 480))

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 固定阈值分割很直接，一句话说就是像素点值大于阈值变成一类值，小于阈值变成另一类值。
# cv2.threshold() 使用该函数做阈值分割

ret, img_th1 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
ret, img_th2 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)
ret, img_th3 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TRUNC)
ret, img_th4 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TOZERO_INV)
ret, img_th5 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TOZERO)

count = 1
for i in [img_th1, img_th2, img_th3, img_th4, img_th5]:
    cv2.imshow(f"img{count}", i)
    count +=1

# cv2.adaptiveThreshold()自适应阈值 会每次取图片的一小部分计算阈值，这样图片不同区域的阈值就不尽相同
img_apath = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
cv2.imshow("img_adapt", img_apath)
while True:
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()

