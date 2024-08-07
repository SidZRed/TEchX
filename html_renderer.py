class HTML_Renderer:
    def __init__ (self, document):
        self.document = document
    
    def render(self):
        return self.render_node(self.document.root)
    
    def render_node(self, node):
        if node.type == 'root':
            return ''.join(self.render_node(child) for child in node.children)
        
        elif node.type == 'section':
            title = node.conten[0]
            content = ''.join(self.render_node(child) for child in node.children)
            return f'<h1>{title}</h1>{content}'
        
        elif node.node_type == 'title':
            return f'<h1>{node.content[0]}</h1>\n'
        
        elif node.node_type == 'author':
            return f'<p><strong>Author:</strong> {node.content[0]}</p>\n'
        
        elif node.node_type == 'date':
            return f'<p><strong>Date:</strong> {node.content[0]}</p>\n'
        
        elif node.node_type == 'text':
            return f'<p>{node.content[0]}</p>\n'
        
        elif node.node_type == 'code':
            language, code = node.content
            return f'<pre><code class="{language}">{code}</code></pre>\n'
        
        elif node.node_type == 'api':
            return f'<h3>API: {node.content[0]}</h3>\n'
        
        elif node.node_type == 'changelog':
            return f'<pre>{node.content[0]}</pre>\n'
        
        else:
            return ''