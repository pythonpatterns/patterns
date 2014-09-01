d = [
    {'a': 1, 'b': 5, 'f': 3, 'd': 4},
    {'a': 1, 'b': 1, 'c': 3, 'd': 4},
    {'d': 4, 'b': 2, 'c': 3, 'e': 1},
]

a = list(set.intersection(*[set(k.values()) for k in d]))
print(a)
"""<
[1, 3, 4]
>"""