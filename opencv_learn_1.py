import cv2
import matplotlib.pyplot as plt
import sys
print(sys.version)

print(cv2.__version__)
img = cv2.imread("./pic/1.png")
# img = cv2.resize(img, (640, 480))

# cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.namedWindow("image", cv2.WINDOW_KEEPRATIO)

cv2.imshow("image",img)

count = 1

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([])
# plt.yticks([])
# plt.show()
while True:

    k = cv2.waitKey(1)
    if k == ord('q'):
        cv2.destroyAllWindows()
        break
    elif k == ord('s'):
        cv2.imwrite("./pic/1_"+str(count)+".png", img) # 对图像保存
        print("save to: "+"./pic/1_"+str(count)+".png")
        count+=1
        k = None
    elif k == ord('g'):
        img_g = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # 将图像转换为灰度
        cv2.namedWindow("image_gray", cv2.WINDOW_NORMAL)
        cv2.imshow("image_gray", img_g)
        cv2.imwrite("./pic/1_"+str(count)+"_gray.png", img_g) # 对图像保存
        print("gray")
        count+=1
cv2.destroyAllWindows()
