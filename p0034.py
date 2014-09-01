n = 3
x = 2

a = [1, 2, 2, 3, 2, 2, 2, 4, 5, 6]

gen = (v for v in a if v != x)
b = [gen.next() for i in range(n)]
print(b)
"""<
[1, 3, 4]
>"""
c = []
for v in a:
    if v != x:
        c.append(v)
    if len(c) == n:
        break
print(c)
"""<
[1, 3, 4]
>"""
