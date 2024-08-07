# intermediate.py

class Node:
    def __init__(self, node_type, content=None):
        self.type = node_type
        self.content = content or []
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class Document:
    def __init__(self):
        self.root = Node('root')

    def add_section(self, section_node):
        self.root.add_child(section_node)

    def __iter__(self):
        return iter(self.root.children)  # Make Document iterable by iterating over root's children
