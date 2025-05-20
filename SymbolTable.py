from var import Var

class SymbolTable():
    symbols = {}

    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}

    def setSymbol(self, key, value):
        self.symbols[key] = value

    
    def getParent(self):
        return self.parent
    
    def setSymbolValue(self, key, value):
        found = False
        table = self
        while True:
            if key in table.symbols:
                found = True
                table.symbols[key] = value
                break
            if table.parent == None:
                break
            table = table.parent
        
        if not found:
            self.symbols[key] = value
    
    def containsSymbol(self, key):
        return key in self.symbols.keys()

    def printTable(self):
        print(self.symbols)

    def getSymbol(self, key):
        if self.parent == None:
            return self.symbols[key]

        if key in self.symbols:
            return self.symbols[key]
        
        return self.parent.getSymbol(key) 
            