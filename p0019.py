a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = [x for x in a if x in b]
print(c)
"""<
[3, 4]
>"""
d = list(set(a) & set(b))
print(d)
"""<
[3, 4]
>"""
e = list(set(a).intersection(b))
print(e)
"""<
[3, 4]
>"""
