from Crypto.Hash import MD5

a = MD5.new('some text').hexdigest()
print(a)
"""<
552e21cd4cd9918678e3c1a0df491bc3
>"""
b = MD5.new()
b.update('some text')
print(b.hexdigest())
"""<
552e21cd4cd9918678e3c1a0df491bc3
>"""
b.update('more text')
print(b.hexdigest())
"""<
cd7a9db4821e0517220108f59a3ed315
>"""