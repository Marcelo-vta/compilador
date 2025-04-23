

class Node():
    def __init__(self, children, value):
        self.children = children
        self.value = value
        return
    
    def Evaluate(self, symbolTable):
        for i in range(len(self.children)):
            self.children[i] = self.children[i].Evaluate(symbolTable)

        
class Block(Node):
    def __init__(self, children):
        super().__init__(children, None)

    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)
        return
    
class BinOp(Node):
    def __init__(self, children, value):
        super().__init__(children, value)

        if len(children) != 2:
            raise ValueError("BinOp should contain two children")
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
        if self.value.value == "||":
            return int(self.children[0] or self.children[1])
        if self.value.value == "&&":
            return int(self.children[0] and self.children[1])
        if self.value.value == "==":
            return int(self.children[0] == self.children[1])
        if self.value.value == ">=":
            return int(self.children[0] >= self.children[1])
        if self.value.value == "<=":
            return int(self.children[0] <= self.children[1])
        if self.value.value == "<":
            return int(self.children[0] < self.children[1])
        if self.value.value == ">":
            return int(self.children[0] > self.children[1])
        raise ValueError("Invalid BinOp value")

class UnOp(Node):
    def __init__(self, children, value):
        super().__init__(children, value)

        if len(children) != 1:
            raise ValueError("UnOp should contain one children")
        return
    
    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)
        if self.value.value == "-":
            return -(self.children[0])
        if self.value.value == "+":
            return self.children[0]
        if self.value.value == "!":
            return not self.children[0]
        if self.value.value == "=":
            return self
        raise ValueError("Invalid UnOp value")
            
class IntVal(Node):
    def __init__(self, value):
        super().__init__([], value)
    
    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)

        if self.value.type == 'identifier':
            self.value.value = symbolTable.getSymbol(self.value.value)
            self.value.type = "postIdentifier"

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

class Print(Node):
    def __init__(self, children):
        super().__init__(children, None)

        if len(children) != 1:
            raise ValueError("Print should contain one children")
        return
    
    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)

        print(self.children[0])
        return
    
class Assignment(Node):
    def __init__(self, children, value):
        super().__init__(children, value)

        if len(children) != 1:
            raise ValueError("Assignment should contain one children")
        return
    
    def Evaluate(self, symbolTable):
        super().Evaluate(symbolTable)

        symbolTable.setSymbol(IntVal(self.value.value), self.children[0])
        return
    
class Conditional(Node):
    def __init__(self, children):
        super().__init__(children, None)

        if len(children) not in [2,3]:
            raise ValueError("conditional should contain two or three children")
        return
    
    def Evaluate(self, symbolTable):
        conditional = self.children[0].Evaluate(symbolTable)

        if conditional:
            self.children[1].Evaluate(symbolTable)
        elif len(self.children) == 3:
            self.children[2].Evaluate(symbolTable)

class WhileLoop(Node):

    def __init__(self, children):
        super().__init__(children, None)

        if len(children) != 2:
            raise ValueError("While should contain two children")
        return
    
    def Evaluate(self, symbolTable):
        conditional = self.children[0].Evaluate(symbolTable)
        while conditional:
            self.children[1].Evaluate(symbolTable)
            conditional = self.children[0].Evaluate(symbolTable)
        return
    
class Input(Node):

    def __init__(self, value=""):
        super().__init__([], value)
        return
    
    def Evaluate(self, symbolTable):
        return int(input(self.value))


    


    

    


    
            
# number1 = IntVal(1)
# number2 = IntVal(2)
# number3 = IntVal(5)
# unop = UnOp([number1], "-")
# operator2 = BinOp([number2, number3], "*")
# operator = BinOp([operator2, unop], "+")
# mainNode = Node([operator], None)

            

