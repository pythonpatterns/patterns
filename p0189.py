from datetime import date
import calendar


def days_in_month(year=None, month=None):
    return calendar.monthrange(
        year or date.today().year,
        month or date.today().month,
    )[1]


"""(
<br />
#### Examples
)"""
print(days_in_month())
"""<
31
>"""
print(days_in_month(2015, 2))
"""<
28
>"""
