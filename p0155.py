from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Table,
    TableStyle
)


def stylesheet():
    # ALIGN: LEFT (default) | CENTER | RIGHT | DECIMAL
    # VALIGN: BOTTOM (default) | MIDDLE | TOP
    return {
        'table_default': TableStyle(
            [
                ('ALIGN', (1, 1), (2, 2), 'RIGHT'),
                ('VALIGN', (-1, 0), (-1, 0), 'MIDDLE'),
                ('VALIGN', (0, 0), (1, 0), 'TOP'),
            ]
        ),
    }


def build_flowables(stylesheet):
    return [
        Table(
            [
                ['foo', 'two\nlines', 3],
                [4, 'some longer text', 6],
                ['spam', 8, 'eggs'],
            ],
            style=stylesheet['table_default'],
        )
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

build_pdf('p0155_1.pdf', build_flowables(stylesheet()))
"""(
> [p0155_1.pdf](/assets/pdf/pp/patterns/p0155_1.pdf)
)"""