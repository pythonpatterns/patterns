a = [1, 2, 3]
b = [4, 5, 6]

c = [(x, y) for x in a for y in b]
print(c)
"""<
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
>"""
import itertools
d = [p for p in itertools.product(a, b)]
print(d)
"""<
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
>"""
