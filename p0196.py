from Crypto.Hash import SHA

a = SHA.new('some text').hexdigest()
print(a)
"""<
37aa63c77398d954473262e1a0057c1e632eda77
>"""
b = SHA.new()
b.update('some text')
print(b.hexdigest())
"""<
37aa63c77398d954473262e1a0057c1e632eda77
>"""
b.update('more text')
print(b.hexdigest())
"""<
f8c9e6242da36a062c0cc2e33a35783c3e80b8a6
>"""