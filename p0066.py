from IPython.html import widgets
from IPython.display import display

btn = widgets.ButtonWidget(description="Click me!")
display(btn)

btn.set_css({
    'width': '120px',
    'height': '60px',
    'font-size': '16px',
})