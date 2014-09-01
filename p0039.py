a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = [x for x in a if not x in b]
print(c)
"""<
[1, 2]
>"""
d = list(set(a) - set(b))
print(d)
"""<
[1, 2]
>"""
e = list(set.difference(set(a), set(b)))
print(e)
"""<
[1, 2]
>"""
