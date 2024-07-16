import numpy as np
import matplotlib.pyplot  as plt
import cv2
import os

path = os.getcwd()
# print(path)
video_path = os.path.join(path, "Opencv_learn", "Practical_pro_1", "video", "cv2_curve.mp4")
print(video_path)
video = cv2.VideoCapture(video_path)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.namedWindow("img_th", cv2.WINDOW_NORMAL)

if not video.isOpened():
    print(f"Error: Could not open video file {video_path}")
else:
    print(f"Successfully opened video file {video_path}")

while True:
    
    ret, frame = video.read()
    if not ret:
        break

    img_blur = cv2.GaussianBlur(frame, [5, 5], 1)
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)
    ret, img_thr = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    img_black = np.zeros((frame.shape[0], frame.shape[1]), np.uint8)
    points = np.array([[500, 350], [int(frame.shape[1]/2), 350], [int(frame.shape[1]/2), frame.shape[0]], [200, frame.shape[0]]])
    img_mask = cv2.fillPoly(img_black, [points], [255])
    img_bit_add = cv2.bitwise_and(img_thr, img_thr,mask=img_mask)
    img_thr_to_RGB = cv2.cvtColor(img_thr, cv2.COLOR_GRAY2BGR)

    contours, n = cv2.findContours(img_bit_add, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img_thr_to_RGB, contours, -1, (255, 0, 0), 2)

    contour_x = []
    contour_y = []

    for contour in contours:
        for con in contour:
            # print(con[0,0])
            contour_x.append(con[0,0])
            contour_y.append(con[0,1])
    # print(contour)
    contour_y_output = [frame.shape[0] - var for var in contour_y]

    x = np.linspace(250, 600, 10)
    fit_out = np.polyfit(contour_x, contour_y_output, 2)
    p = np.poly1d(fit_out)

    fit_point = [(int(x1), frame.shape[0] - int(p(x1))) for x1 in x ]
    fit_points = np.array([fit_point], np.int32)
    cv2.polylines(frame, [fit_points], isClosed=False, color=(0, 255, 0), thickness=2)
    cv2.imshow("img", frame)
    cv2.imshow("img_th", img_bit_add)

    if cv2.waitKey(0) == ord('q'):
        continue
    # print(fit_point)
    # print(fit_points)
video.release()
cv2.destroyAllWindows()

    # plt.figure(1)
    # fig, ((img1, img2), (img3, img4)) = plt.subplots(2, 2)
    # img1.imshow(frame, cmap=None)
    # img2.imshow(img_thr, cmap='gray')
    # img3.imshow(img_bit_add, cmap="gray")
    # img4.imshow(img_thr_to_RGB, cmap='gray')
    # plt.show()

    # plt.figure(2)
    # plt.scatter(contour_x, contour_y_output)
    # plt.plot(x, y_fit, 'red')
    # plt.xlim(0, frame.shape[1])
    # plt.ylim(0, frame.shape[0])
    # plt.tight_layout()
    # plt.show()
