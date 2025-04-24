from var import Var

class SymbolTable():
    symbols = {}
    shift = 0

    def setSymbol(self, key, value=None):
        if key in self.symbols:
            raise Exception("Value already declaired")

        self.shift += 4
        self.symbols[key] = { "value": value, "address": f"[{'EBP' + str(-self.shift)}]" }

        return
    
    def getShift(self, key):
        return self.symbols[key]["address"]
    
    def setSymbolValue(self, key, value):
        self.symbols[key]["value"].value = value
    
    def containsSymbol(self, key):
        return key in self.symbols.keys()

    def printTable(self):
        print(self.symbols)

    def getSymbol(self, key):
        return self.symbols[key]["value"]