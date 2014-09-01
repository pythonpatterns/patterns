d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
l = ['a', 'c']

a = {k: v for k, v in d.items() if k not in l}
print(a)
"""<
{'b': 2, 'd': 4}
>"""
print(d)
"""<
{'a': 1, 'c': 3, 'b': 2, 'd': 4}
>"""
for k in l:
    del(d[k])
print(d)
"""<
{'b': 2, 'd': 4}
>"""
