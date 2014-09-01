import numpy as np
import random

m1 = np.array(
    [
        [random.randint(0, 100) for i in range(3)] 
        for j in range(4)
    ]
)
print(m1)
"""<
[[24 24 91]
 [79  3  5]
 [17 38 86]
 [17  8 73]]
>"""
m2 = np.matlib.rand(4, 3)
print(m2)
"""<
[[ 0.09357887  0.1939389   0.6436383 ]
 [ 0.35710563  0.91332933  0.72869971]
 [ 0.67806313  0.0807419   0.51857413]
 [ 0.02682752  0.5546658   0.59885878]]
>"""
