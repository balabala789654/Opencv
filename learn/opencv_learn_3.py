import cv2
import numpy as np

img = cv2.imread("./pic/3.jpg")
img = cv2.resize(img, (640, 480))
print(img.shape)

cv2.line(img, pt1=(0, 0), pt2=(img.shape[1], img.shape[0]), color=(255, 0, 0), thickness=1) # 画直线

cv2.arrowedLine(img,pt1=(0, img.shape[0]), pt2=(img.shape[1], 0), color=(0, 255, 0), thickness=2)# 画箭头

cv2.rectangle(img=img, pt1=[int(img.shape[1]/2) - 100, int(img.shape[0]/2) - 100], pt2=[int(img.shape[1]/2) + 100, int(img.shape[0]/2) + 100], color=[255, 0, 255], thickness=1)# 画矩形 传参类型为列表 元组都可以

cv2.circle(img, center=(int(img.shape[1]/2), int(img.shape[0]/2)), radius=200, color=(100, 100, 30), thickness=2)# 画圆圈
cv2.imshow("img",img)
 
while True:
    k = cv2.waitKey(0)
    if k == ord('q'):
        break
img.release()