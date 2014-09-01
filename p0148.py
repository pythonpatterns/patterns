from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame, 
    Paragraph
)
from reportlab.lib.styles import ParagraphStyle


def build_pdf(filename):
    doc = BaseDocTemplate(filename)
    doc.addPageTemplates(
        [
            PageTemplate(
                frames=[
                    Frame(
                        doc.leftMargin,    # x
                        doc.bottomMargin,  # y 
                        doc.width,         # frame width
                        doc.height,        # frame height
                        id=None
                    ),
                ]
            ),
        ]
    )
    flowables = [
        Paragraph('some text. ' * 20, ParagraphStyle('default')),
    ]
    doc.build(flowables)

build_pdf('p0148_1.pdf')
"""(
> [p0148_1.pdf](/assets/pdf/pp/patterns/p0148_1.pdf)
)"""
