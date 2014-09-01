import numpy as np

m = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(m)
"""<
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>"""
v = np.diagonal(m)
print(v)
"""<
[1 5 9]
>"""
