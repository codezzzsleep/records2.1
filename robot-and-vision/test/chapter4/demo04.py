import numpy as np

a = np.array([1, 2, 3])
print("正常构造")
print(a)
# -----------------------
a = np.array([[1, 2], [3, 4]])
print("二维构造")
print(a)
# -----------------------
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print("最小维度")
print(a)
# -----------------------
a = np.array([1, 2, 3], dtype=complex)
print("dtype 参数")
print(a)
