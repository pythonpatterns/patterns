import numpy as np

m1 = np.array([[1,2,3], [4,5,6]])
print(m1)
"""<
[[1 2 3]
 [4 5 6]]
>"""
m2 = m1.reshape(3,2)
print(m2)
"""<
[[1 2]
 [3 4]
 [5 6]]
>"""
