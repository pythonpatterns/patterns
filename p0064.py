from IPython.html import widgets
from IPython.display import display

txt = widgets.TextWidget()
display(txt)

txt.value = 'Some Text'

print(txt.value)
"""<
Some Text
>"""
