import numpy as np

v1 = np.array([1,2,3])
print(v1)
"""<
[1 2 3]
>"""
v2 = np.array([4,5,6])
print(v2)
"""<
[4 5 6]
>"""
v3 = np.concatenate((v1,v2))
print(v3)
"""<
[1 2 3 4 5 6]
>"""
