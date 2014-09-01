import math

a = math.log10(5)
print(a)
"""<
0.698970004336
>"""
b = math.log10(10)
print(b)
"""<
1.0
>"""
try:
    c = math.log10(-5)
except ValueError:
    print(':(')
    c = 0
print(c)
"""<
:(
0
>"""
