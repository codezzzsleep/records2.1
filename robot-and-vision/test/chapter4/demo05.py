import numpy as np
# numpy 中的数据类型

# 使用标量类型
dt = np.dtype(np.int32)
print(dt)
# int32

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)
# int32

# 字节顺序标注
dt = np.dtype('<i4')
print(dt)
# int32

# 首先创建结构化数据类型
dt = np.dtype([('age', np.int8)])
print(dt)
# [('age', 'i1')]

# 将数据类型应用于 ndarray 对象
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)
# [(10,) (20,) (30,)]

# 类型字段名可以用于存取实际的 age 列
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])
# [10 20 30]

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
# [('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)
# [(b'abc', 21, 50.) (b'xyz', 18, 75.)]
