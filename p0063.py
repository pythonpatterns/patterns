from IPython.html import widgets
from IPython.display import display

def func(btn):
    print('Hi!')

btn = widgets.ButtonWidget(description="Click me!")
btn.on_click(func)
display(btn)
