from datetime import date
from dateutil import relativedelta


def n_years_ago(n=1, now=None):
    now = now or date.today()
    return now + relativedelta.relativedelta(years=-n)


"""(
<br />
#### Examples
)"""
print(n_years_ago())
"""<
2013-08-30
>"""
print(n_years_ago(5))
"""<
2009-08-30
>"""
