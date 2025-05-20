from var import Var

class SymbolTable():
    symbols = {}

    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}

    def setSymbol(self, key, value, node=None):
        if node != None:
            self.symbols[key] = node
        else:
            self.symbols[key] = value
    
    def getParent(self):
        return self.parent
    
    def setSymbolValue(self, key, value):
        self.symbols[key].value = value
    
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
            