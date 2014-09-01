from datetime import date
from dateutil import relativedelta


def n_months_from_now(n=1, now=None):
    now = now or date.today()
    return now + relativedelta.relativedelta(months=+n)

"""(
<br />
#### Examples
)"""
print(n_months_from_now())
"""<
2014-09-30
>"""
print(n_months_from_now(11))
"""<
2015-07-30
>"""
