from var import Var

class SymbolTable():
    symbols = {}

    def setSymbol(self, key, value):
        self.symbols[key] = value
        return
    
    def setSymbolValue(self, key, value):
        self.symbols[key].value = value
    
    def printTable(self):
        print(self.symbols)

    def getSymbol(self, key):
        return self.symbols[key]