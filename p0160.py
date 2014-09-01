from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Preformatted,
)
from reportlab.lib.styles import ParagraphStyle


def stylesheet():
    return {'default': ParagraphStyle('default'),}


def build_flowables(stylesheet):
    text = """   
foo
    
                        bar
    spam
"""
    
    return [
        Preformatted(text, stylesheet['default'])
    ]

def build_pdf(filename, flowables):
    doc = BaseDocTemplate(filename)
    doc.addPageTemplates(
        [
            PageTemplate(
                frames=[
                    Frame(
                        doc.leftMargin,
                        doc.bottomMargin,
                        doc.width,
                        doc.height,
                        id=None
                    ),
                ]
            ),
        ]
    )
    doc.build(flowables)

build_pdf('p0160_1.pdf', build_flowables(stylesheet()))
"""(
> [p0160_1.pdf](/assets/pdf/pp/patterns/p0160_1.pdf)
)"""
