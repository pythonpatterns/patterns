import math

a = math.log(5, 2)
print(a)
"""<
2.32192809489
>"""
b = math.log(1024, 2)
print(b)
"""<
10.0
>"""
try:
    c = math.log(-5, 2)
except ValueError:
    print(':(')
    c = 0
print(c)
"""<
:(
0
>"""
