import numpy as np

m1 = np.array([[1,2,3], [4,5,6]])
print(m1)
"""<
[[1 2 3]
 [4 5 6]]
>"""
m2 = np.array([[7,8,9], [10,11,12]])
print(m2)
"""<
[[ 7  8  9]
 [10 11 12]]
>"""
m3 = np.hstack((m1,m2))
print(m3)
"""<
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
>"""
