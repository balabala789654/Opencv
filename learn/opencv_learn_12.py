import cv2
import numpy as np

'''
轮廓特征

计算物体的周长、面积、质心、最小外接矩形等
OpenCV 函数：cv2.contourArea(), cv2.arcLength(), cv2.approxPolyDP() 等
'''

path = "./learn/pic/number.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (640, 480))
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret, img_th = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

con, n = cv2.findContours(img_th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_th_rgb = cv2.cvtColor(img_th, cv2.COLOR_GRAY2BGR)

cv2.drawContours(img_th_rgb, con, 1, (0,0,255), 2)

x, y, w, h = cv2.boundingRect(con[1]) # 外接矩形

cv2.rectangle(img_th_rgb, (x,y), (x+w, y+h), (0, 255, 0), 2)

rect = cv2.minAreaRect(con[1])# 最小外接矩形
box = np.int0(cv2.boxPoints(rect))# 矩形的四个角点取整
print(rect,box)
cv2.drawContours(img_th_rgb, [box], 0, (255, 0, 0), 2)# 利用描绘轮廓函数去描绘最小外接矩形

cv2.imshow("img", img_th_rgb)
while True:

    k = cv2.waitKey(1)


    if k == ord('q'):
        break

cv2.destroyAllWindows()