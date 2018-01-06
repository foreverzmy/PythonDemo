# 创建数组
import numpy as np

# 一维数组
a = np.array([0, 1, 2, 3])
print(a, ':', type(a))  # [0 1 2 3] : <class 'numpy.ndarray'>
print('shape:', a.shape)  # shape: (4,)
print(a[0], a[1], a[2], a[3])  # 0 1 2 3
a[0] = 4
print(a)  # [4,1,2,3]

# 二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
# [[1 2 3]
#  [4 5 6]]
print(b.shape)  # (2,3)
print(b[0, 0], b[0, 2], b[1, 0], b[1, 2])  # 1 3 4 6

# 初始化空数组位 0
c = np.zeros((2, 3))
print(c)
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

# 初始化空数组位 1
d = np.ones((2, 3))
print(d)
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

# 初始化数组全为设定值
e = np.full((2, 3), 4)
print(e)
# [[4 4 4]
#  [4 4 4]]

# n * n 单位矩阵
f = np.eye(3)
print(f)
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

# n * n 随机矩阵
g = np.random.random((2, 3))
print(g)
# [[ 0.29913235  0.52457222  0.84490277]
#  [ 0.00589309  0.63422486  0.36840022]]
