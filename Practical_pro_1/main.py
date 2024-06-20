import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

'''
在进行霍夫变换之前，通常需要进行边缘检测。Canny边缘检测是一种常用的方法。
使用霍夫变换检测图像中的直线。
OpenCV提供了两种霍夫变换函数：cv2.HoughLines和cv2.HoughLinesP。
cv2.HoughLinesP是概率霍夫变换，通常更常用，因为它计算效率更高。

'''
def nothing(x):
    pass
def creat_track_th():
    cv2.createTrackbar("th", "img", 0, 255, nothing)
    return None
def creat_track_canny():
    cv2.createTrackbar("maxval", "img_2", 0, 255, nothing)
    cv2.createTrackbar("minval", "img_2", 0, 255, nothing)
    return None
def plt_show(x):
    plt.imshow(x)
    plt.show()
    return None

def img_to_rgb(x):
    return cv2.cvtColor(x, cv2.COLOR_GRAY2BGR)

path = os.getcwd()
path = os.path.join(path, "Practical_pro_1/pic/lane.jpg")
if __name__ == "__main__":
    
    img = cv2.imread(path)
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.namedWindow("img_1", cv2.WINDOW_NORMAL)
    cv2.namedWindow("img_2", cv2.WINDOW_NORMAL)


    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    points = np.array([[399, 340], [564, 340], [885, img.shape[0]], [120, img.shape[0]]])

    img_black = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    mask_img = cv2.fillPoly(img_black, [points], [255])
    ret, img_th = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY)
    img_bit_add = cv2.bitwise_and(img_th,img_th,mask=mask_img)
    img_edge = cv2.Canny(img_bit_add, 200, 255)
    lines = cv2.HoughLinesP(img_edge, 1, np.pi / 180, 15, minLineLength=10, maxLineGap=10)    
    print(len(lines), lines)
    img_color = img_to_rgb(img_edge)
    print(points)
    # creat_track_th()
    # creat_track_canny()

    left_lines = []
    right_lines = []
    average_slope = 0.0
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2-y1)/(x2-x1)
            print(x1, y1, x2, y2, slope)
            cv2.line(img_color, (x1, y1), (x2, y2), (0, 255, 0), 2)    
            cv2.circle(img_color, center=(x1, y1), radius=5, color=(255,0,0), thickness=-1)
            cv2.circle(img_color, center=(x2, y2), radius=5, color=(0,0,255), thickness=-1)
            if slope < 0:
                left_lines.append(slope)
            else:
                right_lines.append(slope)

    for i in range(len(right_lines)):
        average_slope += right_lines[i]

    average_slope = average_slope/len(right_lines)

    print(len(right_lines), right_lines, average_slope)

    while True:
        # num = cv2.getTrackbarPos("th", "img")
        # maxval = cv2.getTrackbarPos("maxval", "img_2")
        # minval = cv2.getTrackbarPos("minval", "img_2")        

        # cv2.polylines(img_color, [points], isClosed=True, color=[255,0,0], thickness=1)
        # con, n = cv2.findContours(img_bit_add, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # cv2.drawContours(img_color, con, -1, [0, 0, 255], 2)

        cv2.imshow("img", img_th)
        cv2.imshow("img_1", mask_img)
        cv2.imshow("img_2", img_color)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break

cv2.destroyAllWindows()