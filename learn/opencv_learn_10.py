import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
# 边缘检测

Canny 边缘检测的简单概念
OpenCV 函数：cv2.Canny()

# cv2.Canny()进行边缘检测，参数 2、3 表示最低、高阈值
# 其实很多情况下，阈值分割后再检测边缘，效果会更好

'''
def nothing(X):
    pass


path = "./pic/3.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (640,480))

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.namedWindow("img_canny", cv2.WINDOW_NORMAL)

cv2.createTrackbar("num", "img", 0, 255, nothing)
cv2.createTrackbar("maxval", "img_canny", 0, 255, nothing)
cv2.createTrackbar("minval", "img_canny", 0, 255, nothing)

while True:
    num = cv2.getTrackbarPos("num", "img")
    ret, img_th = cv2.threshold(img_gray, num, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("img", img_th)

    maxval = cv2.getTrackbarPos("maxval", "img_canny")
    minval = cv2.getTrackbarPos("minval", "img_canny")
    img_edge = cv2.Canny(img_gray, maxval, minval)
    cv2.imshow("img_canny", img_edge)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()