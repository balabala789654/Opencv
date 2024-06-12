import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(1)

while True:
    
    ret, frame = cap.read()
    cv2.imshow("img",frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()