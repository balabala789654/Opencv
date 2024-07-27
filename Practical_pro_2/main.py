import cv2
import os
import numpy as np

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
cv2.namedWindow("out", cv2.WINDOW_NORMAL)

track_bar = ["H1", "S1", "V1", "H2", "S2", "V2"]

red_lower = np.array([114, 49, 225])
red_upper = np.array([179, 252, 255])

def nothing(x):
    pass

def create_Trackbar():
    for x in track_bar:
        if x == "H1" or x == "H2":
            cv2.createTrackbar(x, "HSV", 0, 180, nothing)
        else:
            cv2.createTrackbar(x, "HSV", 0, 255, nothing)
    return None

# track_bar_var = []
def get_Trackbar():
    HSV_ret = [0, 0, 0, 0, 0, 0]
    for x in range(6):
        HSV_ret[x-1] = cv2.getTrackbarPos(track_bar[x-1], "HSV")
    return HSV_ret


video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
video.set(cv2.CAP_PROP_EXPOSURE, -1) # 曝光度
video.set(cv2.CAP_PROP_BRIGHTNESS, 0) # 亮度
video.set(cv2.CAP_PROP_CONTRAST, 0.5) # 对比度
video.set(cv2.CAP_PROP_SATURATION, 0.5) # 饱和度

print(video.get(cv2.CAP_PROP_EXPOSURE), video.get(cv2.CAP_PROP_BRIGHTNESS), video.get(cv2.CAP_PROP_CONTRAST), video.get(cv2.CAP_PROP_SATURATION))

if __name__== "__main__":

    create_Trackbar()
    while True:
        ret_frame, frame = video.read()
        if not ret_frame:
            print("video error")
            break
        frame_blur = cv2.GaussianBlur(frame, (9, 9), 2) # 高斯滤波
        frame_HSV = cv2.cvtColor(frame_blur, cv2.COLOR_RGB2HSV)


        lower = np.array(get_Trackbar()[0:3])
        upper = np.array(get_Trackbar()[3:6])

        mask = cv2.inRange(frame_HSV, lowerb=red_lower, upperb=red_upper)

        frame_bit_add = cv2.bitwise_and(frame, frame, mask=mask)
        
        contours, n = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours=contours, contourIdx=-1, color=(255, 0, 0), thickness=2)
        Circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=200, param1=20, param2=10, minRadius=5, maxRadius=10)
        
        if Circles is not None:
            Circles = np.round(Circles[0, :]).astype("int")

            for [x, y, r] in Circles:
                print("x: ", x, "y: ", y, "r: ", r)
                cv2.circle(frame, [x, y], r, (0, 255, 0), 2)
                

        # print(get_Trackbar(), lower, upper)


        cv2.imshow("frame", frame)
        cv2.imshow("HSV", mask)
        cv2.imshow("out", frame)
        if cv2.waitKey(1) == ord('q'):
            break
video.release()
cv2.destroyAllWindows()

    

