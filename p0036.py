from pprint import pprint
import itertools

a = [[0, 1], [2, 3], [4, 5]]

b = [p for p in itertools.product(*a)]
pprint(b)
"""<
[(0, 2, 4),
 (0, 2, 5),
 (0, 3, 4),
 (0, 3, 5),
 (1, 2, 4),
 (1, 2, 5),
 (1, 3, 4),
 (1, 3, 5)]
>"""
