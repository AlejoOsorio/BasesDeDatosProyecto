from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.colors import Color
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Spacer, Paragraph, PageBreak, Table, TableStyle, Image, SimpleDocTemplate


class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []
        self.width, self.height = LETTER

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            if self._pageNumber > 1:
                self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        page = "Page %s of %s" % (self._pageNumber, page_count)
        x = 128
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.line(30, 740, LETTER[0] - 50, 740)
        self.line(66, 78, LETTER[0] - 66, 78)
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0] - x, 65, page)
        self.restoreState()


class Report:
    def __init__(self, path, headers, content):
        self.path = path
        self.elements = []
        self.content = content
        self.headers = headers

        # colors - Azul turkeza 367AB3
        self.colorOhkaGreen0 = Color((45.0 / 255), (166.0 / 255), (153.0 / 255), 1)
        self.colorOhkaGreen1 = Color((182.0 / 255), (227.0 / 255), (166.0 / 255), 1)
        self.colorOhkaGreen2 = Color((140.0 / 255), (222.0 / 255), (192.0 / 255), 1)
        # self.colorOhkaGreen2 = Color((140.0/255), (222.0/255), (192.0/255), 1)
        self.colorOhkaBlue0 = Color((54.0 / 255), (122.0 / 255), (179.0 / 255), 1)
        self.colorOhkaBlue1 = Color((122.0 / 255), (180.0 / 255), (225.0 / 255), 1)
        self.colorOhkaGreenLineas = Color((50.0 / 255), (140.0 / 255), (140.0 / 255), 1)

        self.first_page()
        self.body_pages_employs()
        self.doc = SimpleDocTemplate(self.path, pagesize=LETTER)
        self.doc.multiBuild(self.elements, canvasmaker=FooterCanvas)

    def first_page(self):
        img = Image('resources/uni.png', kind='proportional', height=0.5 * inch, width=2.4 * inch)
        img.hAlign = 'LEFT'
        self.elements.append(img)

        spacer = Spacer(30, 100)
        self.elements.append(spacer)

        img = Image('resources/img.png', kind='proportional', width=5.5 * inch, height=2.5 * inch)
        self.elements.append(img)

        spacer = Spacer(10, 250)
        self.elements.append(spacer)

        ps_detalle = ParagraphStyle('Resumen', fontSize=9, leading=14, justifyBreaks=1, alignment=TA_LEFT,
                                    justifyLastLine=1)

        date = datetime.now()

        text = """REPORTE DE SERVICIOS PROFESIONALES<br/>
        Empresa: UniBanco<br/>
        Fecha del reporte: %s <br/>
        """ % date.strftime('%d:%m:%Y')
        paragraph_report_summary = Paragraph(text, ps_detalle)
        self.elements.append(paragraph_report_summary)
        self.elements.append(PageBreak())

    def body_pages_employs(self):
        ps_header_text = ParagraphStyle('Hed0', fontSize=12, alignment=TA_LEFT, borderWidth=3,
                                        textColor=self.colorOhkaBlue0)
        text = 'Informe Empleados'
        paragraph_report_header = Paragraph(text, ps_header_text)
        self.elements.append(paragraph_report_header)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)
        """
        Create the line items
        """
        d = []
        header_table = self.headers

        font_size = 8
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in header_table:
            ptext = "<font size='%s'><b>%s</b></font>" % (font_size, text)
            titles_table = Paragraph(ptext, centered)
            d.append(titles_table)
        data = [d]
        formatted_line_data = []

        align_style = [(ParagraphStyle(name=f"0{index}", alignment=TA_CENTER)) for index in range(1, len(data[0]) + 1)]

        for line_data in self.content:
            column_number = 0
            for item in line_data:
                ptext = "<font size='%s'>%s</font>" % (font_size - 1, item)
                p = Paragraph(ptext, align_style[column_number])
                formatted_line_data.append(p)
                column_number = column_number + 1
            data.append(formatted_line_data)
            formatted_line_data = []

        table = Table(data)
        t_style = TableStyle([
            # ('GRID',(0, 0), (-1, -1), 0.5, grey),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            # ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
            ('LINEBELOW', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
            ('BACKGROUND', (0, 0), (-1, 0), self.colorOhkaGreenLineas),
            ('BACKGROUND', (0, -1), (-1, -1), self.colorOhkaBlue1),
            # ('SPAN', (0, -1), (-2, -1)),
        ])

        for j in range(1, len(data)):
            if j % 2 == 0:  # Filas pares
                t_style.add('BACKGROUND', (0, j), (-1, j), colors.lightgrey)
            else:  # Filas impares
                t_style.add('BACKGROUND', (0, j), (-1, j), colors.white)

        table.setStyle(t_style)
        self.elements.append(table)
