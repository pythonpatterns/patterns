import math

a = math.log(5)
print(a)
"""<
1.60943791243
>"""
b = math.log(math.e)
print(b)
"""<
1.0
>"""
try:
    c = math.log(-5)
except ValueError:
    print(':(')
    c = 0
print(c)
"""<
:(
0
>"""
