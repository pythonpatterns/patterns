d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 1, 'b': 2, 'c': 4}

a = list(set(d1.values()) & set(d2.values()))
print(a)
"""<
[1, 2]
>"""