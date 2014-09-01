n = 3

a = [1, 2, 3, 4]
a[n - 1] = 0
print(a)
"""<
[1, 2, 0, 4]
>"""
a = [1, 2, 3, 4]
b = [v if i != n -1 else 0 for i, v in enumerate(a)] 
print(b)
"""<
[1, 2, 0, 4]
>"""
print(a)
"""<
[1, 2, 3, 4]
>"""
