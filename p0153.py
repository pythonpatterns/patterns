from reportlab.lib.colors import HexColor

c1 = HexColor('#ffffff')
print(c1)
"""<
Color(1,1,1,1)
>"""
c2 = HexColor('#FFFFFF')
print(c2)
"""<
Color(1,1,1,1)
>"""
c3 = HexColor('0xffffff')
print(c3)
"""<
Color(1,1,1,1)
>"""
c4 = HexColor('16777215')
print(c4)
"""<
Color(1,1,1,1)
>"""
c5 = HexColor('#FFFFFFFF', hasAlpha=True)
print(c5)
"""<
Color(1,1,1,1)
>"""
c5 = HexColor('#FFFFFF33', hasAlpha=True)
print(c5)
"""<
Color(1,1,1,.2)
>"""