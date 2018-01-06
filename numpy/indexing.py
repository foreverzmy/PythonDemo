# 索引数组
import numpy as np

# Slicing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

b = a[:2, 1:3]
print(b)
# [[2 3]
#  [6 7]]

print(a[0, 1])  # 2
b[0, 0] = 77
print(a[0, 1])  # 77

c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(c)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

row_r1 = c[1, :]
row_r2 = c[1:3, :]
print(row_r1, row_r1.shape)
# [5 6 7 8] (4,)
print(row_r2, row_r2.shape)
# [[5  6  7  8]
#  [9 10 11 12]] (2, 4)

col_r1 = c[:, 1]
col_r2 = c[:, 1:3]
print(col_r1, col_r1.shape)
# [2 6 10] (3,)
print(col_r2, col_r2.shape)
# [[ 2  3]
#  [ 6  7]
#  [10 11]] (3, 1)

f = np.array([[1, 2], [3, 4], [5, 6]])
print(f)
# [[1 2]
#  [3 4]
#  [5 6]]
print(f[[0, 1, 2], [0, 1, 0]])
# [1 4 5]
print(np.array([f[0, 0], f[1, 1], f[2, 0]]))
# [1 4 5]

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(m)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Boolean array indexing
z = np.array([[1, 2], [3, 4], [5, 6]])
print(z)
# [[1 2]
#  [3 4]
#  [5 6]]
bool_idx = (z > 2)
print(bool_idx)
# [[False False]
#  [ True  True]
#  [ True  True]]

print(z[bool_idx])  # [3 4 5 6]
print(z[z > 2])  # [3 4 5 6]
