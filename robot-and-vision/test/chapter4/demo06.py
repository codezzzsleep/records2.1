import numpy as np

a = np.arange(24)
# 返回一个包含 0~23 的一维数组
print(a.ndim)  # a 现只有一个维度
print(a)
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim)
# ndim 属性(秩)
print(b)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
b = a.reshape(3, 2)
print(b)
