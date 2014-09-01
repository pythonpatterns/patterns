max_length = 10

a = [1, 2, 3, 4]

b = a + [0]*(max_length - len(a))
print(b)
"""<
[1, 2, 3, 4, 0, 0, 0, 0, 0, 0]
>"""
