x = 4

a = [1, 2, 3, 4, 4, 5, 6, 1, 4]
for i in range(a.count(x)):
    a.pop(a.index(x))
print(a)
"""<
[1, 2, 3, 5, 6, 1]
>"""
a = [1, 2, 3, 4, 4, 5, 6, 1, 4]
b = [v for v in a if v != x]
print(b)
"""<
[1, 2, 3, 5, 6, 1]
>"""
print(a)
"""<
[1, 2, 3, 4, 4, 5, 6, 1, 4]
>"""
