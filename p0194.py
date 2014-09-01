from Crypto.Hash import HMAC, SHA

key = b'secret key'

a = HMAC.new(key, b'secret text', SHA).hexdigest()
print(a)
"""<
c8dd9650ef1c62c414a6cb0583710a7cd7c3dfd0
>"""
b = HMAC.new(key, digestmod=SHA)
b.update(b'secret text')
print(b.hexdigest())
"""<
c8dd9650ef1c62c414a6cb0583710a7cd7c3dfd0
>"""
