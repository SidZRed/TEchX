class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_pos = 0

    def parse(self):
        document = []
        while self.current_pos < len(self.tokens):
            type, value = self.tokens[self.current_pos]
            if type == 'COMMAND':
                document.append(self.parse_command())
            elif type == 'NEWLINE':
                self.current_pos += 1
            else:
                document.append(('TEXT', value))
                self.current_pos += 1
        return document
    
    def parse_command(self):
        type, value = self.tokens[self.current_pos]
        self.current_pos += 1
        commands = value[1:]
        arguments = []

        if self.current_pos < len(self.tokens) and self.tokens[self.current_pos][0] == 'LBRACE':
            self.current_pos += 1
            argument = ''
            while self.current_pos < len(self.tokens) and self.tokens[self.current_pos][0] != 'RBRACE':
                argument += self.tokens[self.current_pos][1]
                self.current_pos += 1
            arguments.append(argument)
            self.current_pos += 1
        return ('COMMAND', commands, arguments)
    
