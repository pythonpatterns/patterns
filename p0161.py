d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 1, 'b': 2, 'f': 3}

a = list(set(d1.keys()) & set(d2.keys()))
print(a)
"""<
['b']
>"""