import random
import numpy as np

a = random.randint(1, 10)
print(a)
"""<
5
>"""
b = np.random.randint(10)
print(b)
"""<
6
>"""
c = np.random.randint(1, 10)
print(c)
"""<
2
>"""
d = np.random.randint(1, 10, 1)
print(d)
"""<
[8]
>"""
e = np.random.randint(1, 10, 5)
print(e)
"""<
[5 5 9 8 5]
>"""
f = np.random.randint(1, 10, (3, 3))
print(f)
"""<
[[3 9 4]
 [1 9 1]
 [7 7 6]]
>"""
