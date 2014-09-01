a = [1, 2, 3, 4]
b = [[3, 5, 6, 7], [1, 8, 9, 10]]

# a - b[0] - b[1]:

c = [x for x in a if not any([x in l for l in b])]
print(c)
"""<
[2, 4]
>"""
d = list(set(a).difference(*[set(l) for l in b]))
print(d)
"""<
[2, 4]
>"""
