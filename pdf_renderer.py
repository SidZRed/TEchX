from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PDF_Renderer:
    def __init__(self, document, output_file):
        self.document = document
        self.output_file = output_file
        self.c = canvas.Canvas(output_file, pagesize=letter)
        self.width, self.height = letter
        self.y = self.height - 40 

    def render(self):
        self.render_node(self.document.root)
        self.c.save()

    def render_node(self, node):
        if node.node_type == 'root':
            for child in node.children:
                self.render_node(child)
        elif node.node_type == 'section':
            title = node.content[0]
            self.c.setFont("Helvetica-Bold", 14)
            self.c.drawString(40, self.y, title)
            self.y -= 20
            for child in node.children:
                self.render_node(child)
        elif node.node_type == 'title':
            self.c.setFont("Helvetica-Bold", 16)
            self.c.drawString(40, self.y, node.content[0])
            self.y -= 20
        elif node.node_type == 'author':
            self.c.setFont("Helvetica", 12)
            self.c.drawString(40, self.y, f"Author: {node.content[0]}")
            self.y -= 20
        elif node.node_type == 'date':
            self.c.setFont("Helvetica", 12)
            self.c.drawString(40, self.y, f"Date: {node.content[0]}")
            self.y -= 20
        elif node.node_type == 'text':
            self.c.setFont("Helvetica", 12)
            self.c.drawString(40, self.y, node.content[0])
            self.y -= 20
        elif node.node_type == 'code':
            language, code = node.content
            self.c.setFont("Courier", 10)
            self.c.drawString(40, self.y, f"Code ({language}):")
            self.y -= 20
            for line in code.split('\n'):
                self.c.drawString(40, self.y, line)
                self.y -= 15
        elif node.node_type == 'api':
            self.c.setFont("Helvetica-Bold", 12)
            self.c.drawString(40, self.y, f"API: {node.content[0]}")
            self.y -= 20
        elif node.node_type == 'changelog':
            self.c.setFont("Courier", 10)
            self.c.drawString(40, self.y, "Changelog:")
            self.y -= 20
            for line in node.content[0].split('\n'):
                self.c.drawString(40, self.y, line)
                self.y -= 15