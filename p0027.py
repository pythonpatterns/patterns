max_length = 10

a = [1, 2, 3, 4]

b = [0]*(max_length - len(a)) + a
print(b)
"""<
[0, 0, 0, 0, 0, 0, 1, 2, 3, 4]
>"""
