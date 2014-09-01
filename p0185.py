from datetime import date
from dateutil.relativedelta import relativedelta, FR


def next_friday(ref_date=None):
    ref_date = ref_date or date.today()
    return ref_date + relativedelta(weekday=FR)


"""(
<br />
#### Example
)"""
print(next_friday())
"""<
2014-09-05
>"""
print(next_friday(date(2013, 10, 7)))
"""<
2013-10-11
>"""
