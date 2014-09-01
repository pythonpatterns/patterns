a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = [x for x in a if x not in b] + [x for x in b if x not in a]
print(c)
"""<
[1, 2, 5, 6]
>"""
d = list(set(a) ^ set(b))
print(d)
"""<
[1, 2, 5, 6]
>"""
e = list(set(a).symmetric_difference(b))
print(e)
"""<
[1, 2, 5, 6]
>"""
