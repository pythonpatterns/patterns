from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Table
)


def build_flowables():
    return [
        Table(
            [
                [1, 2, 3],
                [4, 'foo', 6],
                [7, 8, 'bar'],
            ]
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

build_pdf('p0154_1.pdf', build_flowables())
"""(
> [p0154_1.pdf](/assets/pdf/pp/patterns/p0154_1.pdf)
)"""
