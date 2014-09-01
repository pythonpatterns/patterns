from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame, 
    Paragraph,
    ListFlowable
)

from reportlab.lib.styles import ParagraphStyle


def stylesheet():
    return {'default': ParagraphStyle('default'),}


def build_flowables(stylesheet):
    return [
        ListFlowable(
            [
                Paragraph('Apple', stylesheet['default']),
                Paragraph('Banana', stylesheet['default']),
                Paragraph('Orange', stylesheet['default']),
            ],
            bulletType='I'  # '1' (default) | 'i' | 'I' | 'a' | 'A'
        ),
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

build_pdf('p0151_1.pdf', build_flowables(stylesheet()))
"""(
> [p0151_1.pdf](/assets/pdf/pp/patterns/p0151_1.pdf)
)"""
