import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
模糊/平滑图片来消除图片噪声
OpenCV 函数：cv2.blur(), cv2.GaussianBlur(), cv2.medianBlur(), cv2.bilateralFilter()

关于滤波和模糊，很多人分不清，我来给大家理理（虽说如此，我后面也会混着用，,ԾㅂԾ,,）：
它们都属于卷积，不同滤波方法之间只是卷积核不同（对线性滤波而言）
低通滤波器是模糊，高通滤波器是锐化

低通滤波器就是允许低频信号通过，在图像中边缘和噪点都相当于高频部分，所以低通滤波器用于去除噪点、平滑和模糊图像。
高通滤波器则反之，用来增强图像边缘，进行锐化处理。

常见噪声有椒盐噪声和高斯噪声，椒盐噪声可以理解为斑点，随机出现在图像中的黑点或白点；
高斯噪声可以理解为拍摄图片时由于光照等原因造成的噪声。
'''

path = "./pic/3.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (640, 480))
blur = cv2.blur(img, (3,3)) # 均值滤波
gaussian = cv2.GaussianBlur(img, (5,5), 1) # 高斯滤波
median = cv2.medianBlur(img, 5) # 中值滤波

cv2.imshow("1", img)
cv2.imshow("2", blur)
cv2.imshow("3", gaussian)
cv2.imshow("4", median)

while True:
    k = cv2.waitKey(1)
    if k ==ord('q'):
        break

cv2.destroyAllWindows()

# plt.imshow(img, cmap='Grays')
# plt.show()
