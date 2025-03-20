class SymbolTable():
    symbols = {}

    def setSymbol(self, key, value):
        self.symbols[key] = value
        return
    
    def getSymbol(self, key):
        return self.symbols[key]