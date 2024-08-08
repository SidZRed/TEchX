from intermediate import Document, Node

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.document = Document()

    def parse(self):
        current_section = None
        while self.pos < len(self.tokens):
            kind, value = self.tokens[self.pos]
            if kind == 'COMMAND':
                command, args = self.parse_command()
                if command == 'section':
                    section_node = Node('section', args)
                    self.document.add_section(section_node)
                    current_section = section_node
                else:
                    node = Node(command, args)
                    if current_section:
                        current_section.add_child(node)
                    else:
                        self.document.root.add_child(node)
            elif kind == 'TEXT':
                text_node = Node('text', value)
                if current_section:
                    current_section.add_child(text_node)
                else:
                    self.document.root.add_child(text_node)
            self.pos += 1
        return self.document

    def parse_command(self):
        kind, value = self.tokens[self.pos]
        self.pos += 1
        command = value[1:]   # Parse after the '~' character
        arguments = []

        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'LBRACE':
            self.pos += 1  # Skip '{'
            argument = ''
            while self.pos < len(self.tokens) and self.tokens[self.pos][0] != 'RBRACE':
                argument += self.tokens[self.pos][1]
                self.pos += 1
            arguments.append(argument)
            self.pos += 1  # Skip '}'

        return command, arguments
