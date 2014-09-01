x = 4
y = 3
a = [1, 2, 3, 5, 3, 6, 2]

try:
    a.insert(a.index(y) + 1, x)
except ValueError:
    a.append(x)
print(a)
"""<
[1, 2, 3, 4, 5, 3, 6, 2]
>"""
a = [1, 2, 3, 5, 3, 6, 2]
try:
    i = a.index(y)
    b = a[:i + 1] + [x] + a[i + 1:]
except ValueError:
    b = a + [x]
print(b)
"""<
[1, 2, 3, 4, 5, 3, 6, 2]
>"""
print(a)
"""<
[1, 2, 3, 5, 3, 6, 2]
>"""
