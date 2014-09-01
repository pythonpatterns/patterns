a = {'a': 1, 'b': 2, 'c': 3}
print(a)
"""<
{'a': 1, 'c': 3, 'b': 2}
>"""
b = {v:k for k, v in a.items()}
print(b)
"""<
{1: 'a', 2: 'b', 3: 'c'}
>"""