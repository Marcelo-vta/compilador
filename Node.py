

class Node():
    def __init__(self, children, value):
        self.children = children
        self.value = value
        return
    
    def Evaluate(self, symbolTable):
        if self.value != None:
            if self.value.type == "identifier":
                self.value.value = symbolTable.getSymbol(self.value.value)
                self.value.type = "postIdentifier"

        for i in range(len(self.children)):
            self.children[i] = self.children[i].Evaluate(symbolTable)

        if len(self.children) != 1:
            return "erro"
        else:
            return(self.children[0])


    
class BinOp(Node):
    def __init__(self, children, value):
        super().__init__(children, value)

        if len(children) != 2:
            raise ValueError("BinOp contains two children")
        return
        
    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)
        if self.value.value == "-":
            return self.children[0] - self.children[1]
        if self.value.value == "+":
            return self.children[0] + self.children[1]
        if self.value.value == "*":
            return self.children[0] * self.children[1]
        if self.value.value == "/":
            return self.children[0] // self.children[1]
        raise ValueError("Invalid BinOp value")

class UnOp(Node):
    def __init__(self, children, value):
        super().__init__(children, value)

        if len(children) != 1:
            raise ValueError("UnOp contains one children")
        return
    
    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)
        if self.value.value == "-":
            return -(self.children[0])
        if self.value.value == "+":
            return self.children[0]
        raise ValueError("Invalid UnOp value")
            
class IntVal(Node):
    def __init__(self, value):
        super().__init__([], value)
    
    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)

        if isinstance(self.value.value, int):
            return self.value.value
        else:
            raise ValueError("IntVal value must be an integer")
        
class NoOp(Node):
    def __init__(self, value):
        super().__init__([], value)

    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)

        return self.value.value

            
# number1 = IntVal(1)
# number2 = IntVal(2)
# number3 = IntVal(5)
# unop = UnOp([number1], "-")
# operator2 = BinOp([number2, number3], "*")
# operator = BinOp([operator2, unop], "+")
# mainNode = Node([operator], None)

            

