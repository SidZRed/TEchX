from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PDF_Renderer:
    def __init__(self, document, output_file):
        self.document = document
        self.output_file = output_file
        self.canvas = canvas.Canvas(output_file, pagesize=letter)
        self.width, self.height = letter
        self.current_y = self.height - 40

    def render_node(self, node):
        if node.type == "title":
            self.canvas.setFont("Helvetica-Bold", 20)
            self.canvas.drawString(40, self.current_y, node.content[0])
            self.current_y -= 30
        elif node.type == "author":
            self.canvas.setFont("Helvetica", 12)
            self.canvas.drawString(40, self.current_y, f"Author: {node.content[0]}")
            self.current_y -= 20
        elif node.type == "date":
            self.canvas.setFont("Helvetica", 12)
            self.canvas.drawString(40, self.current_y, f"Date: {node.content[0]}")
            self.current_y -= 20
        elif node.type == "section":
            self.canvas.setFont("Helvetica-Bold", 16)
            self.canvas.drawString(40, self.current_y, node.content[0])
            self.current_y -= 25
        elif node.type == "text":
            self.canvas.setFont("Helvetica", 12)
            self.canvas.drawString(40, self.current_y, node.content)
            self.current_y -= 15

    def render(self):
        for node in self.document.root.children:
            self.render_node(node)
            for child in node.children:
                self.render_node(child)
        self.canvas.save()
