# 车道检测实战项目
## 介绍
### 图像预处理
> 由于我们使用的是**统计概率霍夫直线变换**然而霍夫直线变换需要输入经过边缘检测后的图像，因此预处理的主要操作是将图像变换成边缘检测图像

>- 使用`cv2.imread`函数读取
>- 使用`cv2.cvtColor`函数转换成灰度
>- 使用`cv2.threshold`函数阈值分割
>- 使用`cv2.Canny`函数边缘检测

>其中创建了一个全黑图像， 使用`cv2.fillPoly` 函数将全黑图像中框出了一个全白区域，使用`cv2.bitwise_and`函数将其与原始图像做了按位与的操作，使图像只在全白区域有显示，在其他区域全黑，起到排除未用信息的作用，即创建一个梯形的 mask 掩膜，然后与边缘检测结果图混合运算，掩膜中白色的部分保留，黑色的部分舍弃。

### 霍夫直线检测
>使用`cv2.HoughLinesP`函数，参数说明：
>- rho：极坐标中rho的分辨率，通常设置为1。
>- theta：极坐标中角度的分辨率，以弧度表示。通常设置为np.pi/180。
>- threshold：阈值，只有累加器中超过该阈值的点才会被认为是直线的一个点。
>- minLineLength：线段的最小长度。比这个长度短的线段会被忽略（仅适用于HoughLinesP）。
>- maxLineGap：允许将同一条直线上的点连接成一条线段的最大间隔（仅适用于HoughLinesP）。

### 车道计算
> 霍尔直线检测后可输出直线的起始点，利用起始点的坐标可将每条直线的斜率计算出来，此时有的直线斜率为正数或为负数， 而斜率为正数的直线为左边车道检测出来的直线，为负的为右边车道
>利用该特性可将左右车道的起始点分割开来

>在做完直线左右车道的分割后，使用`np.polyfit`函数做最小二乘法进行线性拟合，即将同一车道上检测出来的所有点拟合成一对起始点，`np.polyfit`函数返回的是拟合直线的斜率以及y轴的截距，利用`np.poly1d`函数通过输入`np.polyfit`函数返回的参数，可创建创建多项式函数。

>至此，车道检测完毕

## 主要代码
### 预处理
```
def image_process():
    global img, img_th
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
    return img_edge
```
### 霍夫直线检测
```
lines = cv2.HoughLinesP(img_edge, 1, np.pi / 180, 15, minLineLength=10, maxLineGap=10)
```

### 车道计算
#### 拟合函数
```
def fit_output(_points, ymax, ymin):
    x_fit = [p[0] for p in _points]
    y_fit = [p[1] for p in _points]

    fit = np.polyfit(y_fit,x_fit,1)
    fit_fn = np.poly1d(fit)
    # print(type(fit), fit, type(fit_fn),fit_fn)
    xmin = int(fit_fn(ymin))
    xmax = int(fit_fn(ymax))

    return [(xmin, ymin), (xmax, ymax)]
```
#### main
```
    left_lines = []
    right_lines = []
    average_slope = 0.0
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2-y1)/(x2-x1)
            print(x1, y1, x2, y2, slope)
            cv2.line(img_color, (x1, y1), (x2, y2), (0, 255, 0), 2)    
            cv2.circle(img_color, center=(x1, y1), radius=2, color=(255,0,0), thickness=-1)
            cv2.circle(img_color, center=(x2, y2), radius=2, color=(0,0,255), thickness=-1)
            if slope < 0:
                left_lines.append(line)
            else:
                right_lines.append(line)

    print(left_lines, "\n")
    left_points = [(x1,y1) for line in left_lines for x1, y1, x2, y2 in line]
    left_points = left_points + [(x2, y2) for line in left_lines for x1, y1, x2, y2 in line]

    right_points = [(x1, y1) for line in right_lines for x1, y1, x2, y2 in line]
    right_points = right_points + [(x2, y2) for line in right_lines for x1, y1, x2, y2 in line]

    print(type(left_lines), left_points)

    point_left_fit_1, point_left_fit_2 = fit_output(left_points, img.shape[0], 340)
    point_right_fit_1, point_right_fit_2 = fit_output(right_points, img.shape[0], 340)
```




