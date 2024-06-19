import cv2
import numpy as np

'''

了解轮廓概念
寻找并绘制轮廓
OpenCV 函数：cv2.findContours(), cv2.drawContours()


cv2.findContours()
参数 2：轮廓的查找方式，一般使用 cv2.RETR_TREE，表示提取所有的轮廓并建立轮廓间的层级。更多请参考：RetrievalModes
参数 3：轮廓的近似方法。比如对于一条直线，我们可以存储该直线的所有像素点，也可以只存储起点和终点。
    使用 cv2.CHAIN_APPROX_SIMPLE 就表示用尽可能少的像素点表示轮廓。更多请参考：ContourApproximationModes
简便起见，这两个参数也可以直接用真值 3 和 2 表示。


cv2.drawContours()
其中参数 2 就是得到的 contours，
参数 3 表示要绘制哪一条轮廓，-1 表示绘制所有轮廓，
参数 4 是颜色（B/G/R 通道，所以(0,0,255) 表示红色），
参数 5 是线宽，之前在绘制图形中介绍过。

'''
def nothing(X):
    pass

path = "./pic/3.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (640, 480))

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.createTrackbar("num", "img", 0, 255, nothing)

while True:
    k = cv2.waitKey(1)
    num = cv2.getTrackbarPos("num", "img")
    ret, img_th = cv2.threshold(img_gray, num, 255, cv2.THRESH_BINARY)
    

    contours, n = cv2.findContours(img_th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 返回的第一个参数为轮廓点

    # print(n)
    img_th_rgb = cv2.cvtColor(img_th, cv2.COLOR_GRAY2BGR) # 将阈值分割后的二值图片转换成rgb图片 在对其做轮廓描绘 即可在图片中显示红色的轮廓图
    cv2.drawContours(img_th_rgb, contours, -1, (0, 0, 255), 1)

    cv2.imshow("img", img_th_rgb)
    if k == ord('q'):
        break
cv2.destroyAllWindows()