# 1. 导入模块
import numpy as np
import mglearn
import matplotlib.pyplot as plt

# 2. 生成身高和体重数据集

X = np.array([[1.5, 48], [1.5, 51], [1.6, 50], [1.65, 62], [1.70, 66], [1.80, 72]])
y = np.array([1, 1, 1, 0, 0, 0])
# 3. 对数据集作图
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Men", "Women"])
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()


