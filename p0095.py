import numpy as np

m = np.array([[i // j for i in range(5)] for j in range(1, 4)])
print(m)
"""<
[[0 1 2 3 4]
 [0 0 1 1 2]
 [0 0 0 1 1]]
>"""
