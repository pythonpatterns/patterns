from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Table,
    TableStyle
)
from reportlab.lib import colors


def stylesheet():
    return {
        'table_default': TableStyle(
            [
                ('BACKGROUND', (0, 0), (2, 2), colors.violet),
                ('ROWBACKGROUNDS', (0, 4), (2, -1), [
                    colors.lightgrey, colors.white
                ]),
                ('COLBACKGROUNDS', (3, 3), (-1, 3), [
                    colors.red, colors.yellow, colors.blue
                ]),
                ('ROWBACKGROUNDS', (5, 5), (-1, -1), [
                    colors.gray, colors.yellow
                ]),
                ('COLBACKGROUNDS', (5, 5), (-1, -1), [
                    None, colors.yellow
                ]),
            ]
        ),
    }


def build_flowables(stylesheet):
    return [
        Table(
            [[i for i in range(10)] for j in range(10)],
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

build_pdf('p0159_1.pdf', build_flowables(stylesheet()))
"""(
> [p0159_1.pdf](/assets/pdf/pp/patterns/p0159_1.pdf)
)"""
