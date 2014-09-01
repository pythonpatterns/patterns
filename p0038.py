a = [[1, 2, 3, 4], [3, 4, 5, 6], [1, 6, 7, 8]]

b = list(set.union(*[set(l) for l in a]))
print(b)
"""<
[1, 2, 3, 4, 5, 6, 7, 8]
>"""
import itertools
c = [x for x in set(itertools.chain(*a))]
print(c)
"""<
[1, 2, 3, 4, 5, 6, 7, 8]
>"""
