a = [[1, 2, 3, 4], [3, 4, 5, 6], [1, 5, 7, 8]]

b = a[0]
for i in range(len(a) - 1):
    b = list(set(b) ^ set(a[i + 1]))
print(b)
"""<
[2, 6, 7, 8]
>"""
tmp = {}
for v in [i for s in a for i in s]:
    tmp[v] = (v not in tmp)
c = [k for k, v in tmp.iteritems() if v]
print(c)
"""<
[2, 6, 7, 8]
>"""
