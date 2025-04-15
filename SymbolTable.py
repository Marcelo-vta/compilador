class SymbolTable():
    symbols = {}

    def setSymbol(self, key, value):
        self.symbols[key.value] = value
        return
    
    def printTable(self):
        print(self.symbols)

    def getSymbol(self, key):
        return self.symbols[key]