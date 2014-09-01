import math

a = math.sqrt(9)
print(a)
"""<
3.0
>"""
try:
    b = math.sqrt(-9)
except ValueError:
    print(':(')
    b = 0
print(b)
"""<
:(
0
>"""
