import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
# cap1 = cv2.VideoCapture(1)

def nothing(x):
    pass

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.createTrackbar("th", "img", 0, 255, nothing)
while cap.isOpened():
    
    ret, frame = cap.read()
    # ret1, frame1 = cap1.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    th = cv2.getTrackbarPos("th", "img")
    ret1, frame_th = cv2.threshold(frame, th, 255, cv2.THRESH_BINARY)

    print(frame.shape, "fps: ", cap.get(cv2.CAP_PROP_FPS))
    if ret:
        cv2.imshow("img",frame_th)       
    k = cv2.waitKey(1)

    if k == ord('q'):
        break

cap.release()
# cap1.release()
cv2.destroyAllWindows()