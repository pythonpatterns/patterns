d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 1, 'b': 2, 'c': 4}

a = list(set(d1.items()) & set(d2.items()))
print(a)
"""<
[('b', 2)]
>"""