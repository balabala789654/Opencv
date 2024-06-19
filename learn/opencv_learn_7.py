import cv2
import numpy as np
import random
path = "./pic/3.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (640, 480))
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def nothing(x):
    pass

cv2.namedWindow("img")
cv2.createTrackbar("num", "img", 0, 255, nothing)

print(img_gray.shape, img_gray.ndim)

img_threshold = np.zeros((480, 640), np.uint8)

def my_img_threshold(x: int):
    for i in range(img_gray.shape[0]):
        for j in range(img_gray.shape[1]):
            if img_gray[i,j] < x:
                img_threshold[i,j] = 0
            else:
                img_threshold[i,j] = 255
    return None



# 自己写的阈值分割算法 可通过调整滑动条来改变阈值分割效果

while True:
    num = cv2.getTrackbarPos("num", "img")
    # print(num)
    my_img_threshold(num)
    
    # print(img_gray[random.randint(0, 100), random.randint(0,200)])

    cv2.imshow("img", img_threshold)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break
cv2.destroyAllWindows()

