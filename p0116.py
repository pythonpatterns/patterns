import math

a = math.factorial(5)
print(a)
"""<
120
>"""
try:
    b = math.factorial(-5)
except ValueError:
    print(':(')
    b = 0
print(b)
"""<
:(
0
>"""
