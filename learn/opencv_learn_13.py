'''
   本程序根据2023年全国电子设计竞赛e题
   识别矩形
'''
import cv2
import numpy as np

def nothing(x):
    pass

cap  =cv2.VideoCapture(0)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.createTrackbar("n", "img", 0, 255, nothing)

while True:
    ret, frame = cap.read()
    n = cv2.getTrackbarPos("n", "img")

    img_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret, img_th = cv2.threshold(img_gray, n, 255, cv2.THRESH_BINARY)
    img_rgb = cv2.cvtColor(img_th, cv2.COLOR_GRAY2BGR)

    contours, hierarchy = cv2.findContours(img_th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        peri = cv2.arcLength(contour, True) # 计算周长
        approx = cv2.approxPolyDP(contour, 0.1 * peri, True) # 轮廓近似

        if len(approx) == 4:
            cv2.drawContours(img_rgb, [approx], -1, (255, 0, 0), 2)
    # cv2.drawContours(img_rgb, contours, -1, (0,255,0), 1)
    
    cv2.imshow("img", img_rgb)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()