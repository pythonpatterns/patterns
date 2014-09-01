import numpy as np

m1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(m1)
"""<
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>"""
m2 = np.triu(m1)
print(m2)
"""<
[[1 2 3]
 [0 5 6]
 [0 0 9]]
>"""
