class Code:
    instructions = []

    def append(self, code: str):
        self.instructions.append(code)
    
    def dump(self, filename):
        with open(filename, 'w') as file:
            file.write("\n".join(self.instructions))