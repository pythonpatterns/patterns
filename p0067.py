from IPython.html import widgets
from IPython.display import display

options = {
    'first value' : 0,
    'second value': 1,
    'third value': 2,
}

s = widgets.SelectWidget()
s.values = options
display(s)

d = widgets.DropdownWidget()
d.values = options
display(d)