import cv2
import numpy as np

img_path = "./pic/color_block.jpg"
# img = np.zeros([480, 640, 3], np.uint8)
img = cv2.imread(img_path)
img = cv2.resize(img, (640, 480))
def nothing(X):
    pass

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.namedWindow("img_1")
cv2.namedWindow("img_2")


cv2.createTrackbar("r", "img", 0, 255, nothing)
cv2.createTrackbar("g", "img", 0, 255, nothing)
cv2.createTrackbar("b", "img", 0, 255, nothing)

cv2.createTrackbar("rl", "img", 0, 255, nothing)
cv2.createTrackbar("gl", "img", 0, 255, nothing)
cv2.createTrackbar("bl", "img", 0, 255, nothing)

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

print(img)

while True:
    r = cv2.getTrackbarPos("r", "img")
    g = cv2.getTrackbarPos("g", "img")
    b = cv2.getTrackbarPos("b", "img")

    rl = cv2.getTrackbarPos("rl", "img")
    gl = cv2.getTrackbarPos("gl", "img")
    bl = cv2.getTrackbarPos("bl", "img")

    mask = cv2.inRange(img_hsv, np.array([r,g,b]), np.array([rl,gl,bl]))# 根据阈值构建掩模
    res = cv2.bitwise_and(img, img, mask) # 对原图像和掩模位运算
    # img = cv2.merge([h,s,v])
    # print(img.shape)

    cv2.imshow("img_1", mask)
    cv2.imshow("img_2", res)
    # cv2.imshow("img_3", res)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()