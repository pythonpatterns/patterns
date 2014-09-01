import string

a = "Hi! I'm Steve."

b = a.translate(None, string.punctuation)
print(b)
"""<
Hi Im Steve
>"""
