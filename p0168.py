d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

a = {k: v for k, v in d.items() if v > 2}
print(a)
"""<
{'c': 3, 'd': 4}
>"""