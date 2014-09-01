a = [[1, 2, 3, 4], [3, 4, 5, 6], [1, 3, 7, 8]]

b = list(set.intersection(*[set(l) for l in a]))
print(b)
"""<
[3]
>"""
c = [x for x in a[0] if all([x in l for l in a[1:]])]
print(c)
"""<
[3]
>"""
