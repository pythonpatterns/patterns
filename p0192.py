from Crypto.Hash import HMAC

key = b'secret key'


a = HMAC.new(key, b'secret text').hexdigest()
print(a)
"""<
030e3d8bbedfbcab54d8148c587782b5
>"""
b = HMAC.new(key)
b.update(b'secret text')
print(b.hexdigest())
"""<
030e3d8bbedfbcab54d8148c587782b5
>"""
