from datetime import datetime
from dateutil.relativedelta import relativedelta


def timespan(dt1, dt2=None):
    delta = relativedelta(dt1, dt2 or datetime.now())
    for i, s in enumerate([
        'years',
        'months',
        'days',
        'hours',
        'minutes',
        'seconds',
    ]):
        v = abs(getattr(delta, s))
        if v > 0:
            return '%i %s' % (v, s if v != 1 else s[:-1])
    return '0 seconds'


"""(
<br />
#### Example
)"""
print(
    'This book was published %s ago.' % timespan(
        datetime(2003, 11, 2)
    )
)
"""<
This book was published 10 years ago.
>"""
