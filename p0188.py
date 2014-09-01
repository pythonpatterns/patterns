from datetime import date
from dateutil.relativedelta import relativedelta, FR
import calendar


def last_friday_of_month(ref_date=None):
    ref_date = ref_date or date.today()
    return ref_date + relativedelta(
        day=calendar.monthrange(ref_date.year, ref_date.month)[1],
        weekday=FR(-1)
    )


"""(
<br />
#### Examples
)"""
print(last_friday_of_month())
"""<
2014-08-29
>"""
print(last_friday_of_month(date(2015, 2, 19)))
"""<
2015-02-27
>"""
