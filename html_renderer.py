class HTML_Renderer:
    def __init__(self, document):
        self.document = document

    def render_node(self, node):
        if node.type == "title":
            return f"<h1>{node.content[0]}</h1>\n"
        elif node.type == "author":
            return f"<p><strong>Author:</strong> {node.content[0]}</p>\n"
        elif node.type == "date":
            return f"<p><strong>Date:</strong> {node.content[0]}</p>\n"
        elif node.type == "section":
            return f"<h2>{node.content[0]}</h2>\n"
        elif node.type == "text":
            return f"<p>{node.content}</p>\n"
        else:
            return ""

    def render(self):
        html = "<html><body>\n"
        for node in self.document.root.children:  # Iterate over nodes
            html += self.render_node(node)
            for child in node.children:  # Render children nodes
                html += self.render_node(child)
        html += "</body></html>"
        return html
