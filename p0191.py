from Crypto.Hash import SHA256

a = SHA256.new('some text').hexdigest()
print(a)
"""<
b94f6f125c79e3a5ffaa826f584c10d52ada669e6762051b826b55776d05aed2
>"""
b = SHA256.new()
b.update('some text')
print(b.hexdigest())
"""<
b94f6f125c79e3a5ffaa826f584c10d52ada669e6762051b826b55776d05aed2
>"""
b.update('more text')
print(b.hexdigest())
"""<
e6ea606424922dff46fe66603e9dce52cba1c2e6893ee10dd22a2679ba6fd406
>"""