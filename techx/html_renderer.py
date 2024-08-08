from datetime import date

class HTML_Renderer:
    def __init__(self, document):
        self.document = document

    def render_node(self, node):
        if node.type == "title":
            return f"<h1 style=\"text-align: center;\">{node.content[0]}</h1>\n"
        elif node.type == "author":
            return f"<p><strong>Author:</strong> {node.content[0]}</p>\n"
        elif node.type == "date":
            if (len(node.content) == 0):
                date_today = date.today()
                return f"<p><strong>Date:</strong> {date_today}</p>\n"
            return f"<p><strong>Date:</strong> {node.content[0]}</p>\n"
        elif node.type == "section":
            return f"<h2>{node.content[0]}</h2>\n"
        elif node.type == "code":
            code_content = node.content[0]
            language = code_content.split(':')[0]
            code = code_content.split(':')[1]
            return f"<pre><code class=\"language-{language}\">{code}</code></pre>\n"
        elif node.type == "api":
            return f"<p><strong>API:</strong> {node.content[0]}</p>\n"
        elif node.type == "changelog":
            return f"<p><strong>Changelog:</strong> {node.content[0]}</p>\n"
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
