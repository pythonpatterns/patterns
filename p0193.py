from Crypto.Hash import HMAC, SHA256

key = b'secret key'

a = HMAC.new(key, b'secret text', SHA256).hexdigest()
print(a)
"""<
dd8521ac3bdb59d9c4f6fcb4a3a14d9cf586dd30b63e6b1dafab18f059fdcc6c
>"""
b = HMAC.new(key, digestmod=SHA256)
b.update(b'secret text')
print(b.hexdigest())
"""<
dd8521ac3bdb59d9c4f6fcb4a3a14d9cf586dd30b63e6b1dafab18f059fdcc6c
>"""
