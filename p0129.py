import math

a = math.hypot(3, -3)
print(a)
"""<
4.24264068712
>"""
p = (3, -3)
b = math.hypot(*p)
print(b)
"""<
4.24264068712
>"""
