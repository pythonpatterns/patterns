from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Table,
)
from reportlab.lib.units import cm


def build_flowables():
    data = [[i for i in range(3)] for j in range(3)]
    return [
        Table(
            data,
        ),
        Table(
            data,
            None,
            len(data) * [1 * cm]
        ),
        Table(
            data,
            None,
            [h * cm for h in [2, 0.5, 3]]
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

build_pdf('p0158_1.pdf', build_flowables())
"""(
> [p0158_1.pdf](/assets/pdf/pp/patterns/p0158_1.pdf)
)"""
