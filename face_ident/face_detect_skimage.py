"""
利用skimage来计算图像的HOG(方向梯度直方图)
"""
# 人脸探测
# 1.导入库函数
from skimage import io, color
from skimage.feature import hog
import matplotlib.pyplot as plt
from skimage import io
import dlib
# 2. 导入图片
image = io.imread("yui1.jpg")
image = color.rgb2gray(image)

# 3. 计算HOG
# hog()返回值
# 1-array HOG
# hog_image(可用于显示hog图)
arr, hog_image = hog(image, visualize=True, orientations=4)

# 4. 作图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(image, cmap=plt.gray())
ax2.imshow(hog_image, cmap=plt.gray())
plt.show()

# 人脸探测
# 人脸标识


# 1.获取图片,转换成数组
file_name = "yui1.jpg"
image = io.imread(file_name)

# 3 建立人脸探测器
detector = dlib.get_frontal_face_detector()

# 4 运行在图片数据上
detected_faces = detector(image, 1)
print("发现{}张人脸, 于{}图片.".format(len(detected_faces), file_name))
# 5.人脸"68点-预测" 模型
model = "shape_predictor_68_face_landmarks.dat"

# 提取特征
predictor = dlib.shape_predictor(model)

# 6. 建立窗口
win = dlib.image_window()
win.set_image(image)

# 5.对每张人脸,操作
# for 循环, 实现人脸探测和标识
# enumerate() 返回迭代对象的索引和对应的值
for i, box in enumerate(detected_faces):
    win.add_overlay(box)
    print("第{}张人脸的位置:{},右边位置:{}.".format(i + 1, box.left(), box.right()))
    landmarks = predictor(image, box)
    win.add_overlay(landmarks)
    dlib.hit_enter_to_continue()

