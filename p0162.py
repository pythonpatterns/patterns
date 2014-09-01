d = [
    {'a': 1, 'b': 2, 'f': 3, 'd': 4},
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
    {'d': 1, 'b': 2, 'c': 3, 'e': 4},
]

a = list(set.intersection(*[set(k.keys()) for k in d]))
print(a)
"""<
['b', 'd']
>"""