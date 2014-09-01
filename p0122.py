import math

a = math.exp(3)
print(a)
"""<
20.0855369232
>"""
b = math.e ** 3
print(b)
"""<
20.0855369232
>"""
try:
    c = math.exp(1000)
except OverflowError:
    print(':(')
    c = 0
print(c)
"""<
:(
0
>"""
