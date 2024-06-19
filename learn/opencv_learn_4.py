import cv2
import numpy as np
def nothing(x):
    pass

img_path = "./pic/3.jpg"

x = 1
y = 1

# img = np.zeros((640, 480, 3), np.uint8)
img = cv2.imread(img_path)
img = cv2.resize(img, (640,480))
cv2.namedWindow("img", cv2.WINDOW_NORMAL)

# 创建滑动条做调色板
cv2.createTrackbar("r", "img", 0, 255, nothing)
cv2.createTrackbar("g", "img", 0, 255, nothing)
cv2.createTrackbar("b", "img", 0, 255, nothing)

print(img[480-1][640-1], type(img), type(img[480-1][640-1][0]))
while True:
    r = cv2.getTrackbarPos("r", "img")
    g = cv2.getTrackbarPos("g", "img")
    b = cv2.getTrackbarPos("b", "img")

    # tip: 在opencv python中图像的img[:,:,2]为红色分量，img[:,:,1]为绿色分量，img[:,:,0]为蓝色分量 
    img[:, :] = [b,g,r] 

    cv2.imshow("img",img)
    # print(img[x][y][0], type(img), type(img[x][y][0]))
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    elif k == ord('p'):
        print(img[1,1])
cv2.destroyAllWindows()
img.release()