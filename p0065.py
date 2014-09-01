from IPython.html import widgets
from IPython.display import display

btn = widgets.ButtonWidget(description="Click me!")
display(btn)

btn.add_class('btn-primary')