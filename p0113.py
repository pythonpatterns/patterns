a = 3 / 2
print(a)
"""<
1        Python 2.x
1.5      Python 3
>"""
b = 3.0 / 2
print(b)
"""<
1.5
>"""
c = 16 / 4 / 2
print(c)
"""<
2
>"""
import operator as op
d = reduce(op.div, [2, 3, 4], 120) # 120 / 2 / 3 / 4
print(d)
"""<
5
>"""
