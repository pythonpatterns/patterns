a = 3 * 2
print(a)
"""<
6
>"""
b = 3 * 2.5
print(b)
"""<
7.5
>"""
c = 2 * 3 * 4
print(c)
"""<
24
>"""
import operator as op
d = reduce(op.mul, [2, 3, 4, 5], 1)
print(d)
"""<
120
>"""
