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
            max([len(r) for r in data]) * [2 * cm]
        ),
        Table(
            data,
            [w * cm for w in [3, 1, 5]]
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

build_pdf('p0157_1.pdf', build_flowables())
"""(
> [p0157_1.pdf](/assets/pdf/pp/patterns/p0157_1.pdf)
)"""
