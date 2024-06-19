import cv2
import numpy as np

img1 = cv2.imread("./pic/1.png")
img2 = cv2.imread("./pic/2.jpg")

print(img1.shape, img2.shape)
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

print(img1.shape, img2.shape)

img_add = cv2.add(img1, img2) # 图像普通相加
img_add_1 = cv2.addWeighted(img1, 0.8, img2, 0.2, 0) # 图像权值相加 第一张图的权值为0.8 第二张图的权值为0.2
# cv2.namedWindow("img")
cv2.imshow("img", img_add)
cv2.imshow("img1", img_add_1)

def nothing():
    pass
while True:
    e1 = cv2.getTickCount() # 获取计数
    for i in range(200):
        for j in range(100):
            nothing()

    e2 = cv2.getTickCount() # 获取计数
    T = (e2 - e1) / cv2.getTickFrequency() # 获取时钟频率 从而计算周期
    print(e1,e2,"T: ", T)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()