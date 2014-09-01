from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame, 
    Paragraph,
    ListFlowable
)
from reportlab.lib.colors import (
    black,
    purple
)
from reportlab.lib.styles import ParagraphStyle, ListStyle


def stylesheet():
    styles = {
        'default': ParagraphStyle('default'),
        'list_default': ListStyle(
            'list_default',
            leftIndent=18,
            rightIndent=0,
            spaceBefore=0,
            spaceAfter=0,
            bulletAlign='left',
            bulletType='1',
            bulletColor=black,
            bulletFontName='Helvetica',
            bulletFontSize=12,
            bulletOffsetY=0,
            bulletDedent='auto',
            bulletDir='ltr', 
        )
    }
    styles['list_special'] = ListStyle(
        'list_special',
        parent=styles['list_default'],
        spaceBefore=12,
        spaceAfter=12,
        bulletColor='purple',
        bulletFontName='Courier-Bold',
        bulletFontSize=8,
        bulletOffsetY=-1,
        bulletDedent=-180,
        bulletDir='rtl',
        bulletType='I',
    )
    return styles


def build_flowables(stylesheet):
    return [
        Paragraph('Some text.', stylesheet['default']),
        ListFlowable(
            [
                Paragraph('Apple', stylesheet['default']),
                Paragraph('Banana', stylesheet['default']),
                Paragraph('Orange', stylesheet['default']),
            ],
            style=stylesheet['list_default'],
        ),
        Paragraph('More text.', stylesheet['default']),
        ListFlowable(
            [
                Paragraph('Apple', stylesheet['default']),
                Paragraph('Banana', stylesheet['default']),
                Paragraph('Orange', stylesheet['default']),
            ],
            style=stylesheet['list_special'],
            start=5
        ),
        Paragraph('Even more text.', stylesheet['default']),
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

build_pdf('p0152_1.pdf', build_flowables(stylesheet()))
"""(
> [p0152_1.pdf](/assets/pdf/pp/patterns/p0152_1.pdf)
)"""