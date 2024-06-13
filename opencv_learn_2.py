import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

while cap.isOpened() and cap1.isOpened():
    
    ret, frame = cap.read()
    ret1, frame1 = cap1.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    print(frame.shape, "fps: ", cap.get(cv2.CAP_PROP_FPS))
    if ret:
        cv2.imshow("img",frame)
    if ret1:
        cv2.imshow("img1", frame1)
        
    k = cv2.waitKey(1)

    if k == ord('q'):
        break

cap.release()
cap1.release()
cv2.destroyAllWindows()