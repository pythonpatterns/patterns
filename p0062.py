from datetime import datetime

dt = datetime(2013, 6, 26, 13, 45, 23)

iso = dt.strftime("%Y-%m-%dT%H:%M:%S")
print(iso)
"""<
2013-06-26T13:45:23
>"""
