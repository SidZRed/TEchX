class Node:
    def __init__(self, type, content=None):
        self.type = type
        if content:
            self.content = content
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    def __repr__(self):
        return f'Node({self.type}, {self.content}, {self.children})'


class Document:
    def __init__(self):
        self.root = Node('root')
    
    def add_section(self, title):
        section = Node('section', title)
        self.root.add_child(section)
    
    def __repr__(self):
        return f'Document({self.root})'
