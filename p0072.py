import string
import random

length = 24

s = ''.join(
    [
        random.choice(
            string.ascii_uppercase + string.digits
        ) for i in range(length)
    ]
)
print(s)
"""<
4G2QYWDY251454LZTU43TVEE
>"""
