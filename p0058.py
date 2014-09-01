from datetime import date, timedelta

d = date(2010, 5, 16)

three_days_earlier = d - timedelta(days=3)

print(three_days_earlier)
"""<
2010-05-13
>"""
