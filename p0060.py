from datetime import date, datetime

d = date(2013, 5, 25)

dt = datetime.combine(d, datetime.min.time())

print(dt)
"""<
2013-05-25 00:00:00
>"""
