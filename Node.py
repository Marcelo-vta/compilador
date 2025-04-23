

class Node():
    def __init__(self, children, value):
        self.children = children
        self.value = value
        return
    
    def Evaluate(self, symbolTable):
        pass

        
class Block(Node):
    def Evaluate(self, symbolTable):
        for child in self.children:
            child.Evaluate(symbolTable)
    
class BinOp(Node):
        
    def Evaluate(self, symbolTable):

        left = self.children[0].Evaluate(symbolTable)
        right = self.children[1].Evaluate(symbolTable)

        if self.value == "-":
            return left - right 
        if self.value == "+":
            return left + right
        if self.value == "*":
            return left * right
        if self.value == "/":
            return left // right
        if self.value == "||":
            return int(left or right)
        if self.value == "&&":
            return int(left and right)
        if self.value == "==":
            return int(left == right)
        if self.value == ">=":
            return int(left >= right)
        if self.value == "<=":
            return int(left <= right)
        if self.value == "<":
            return int(left < right)
        if self.value == ">":
            return int(left > right)

class UnOp(Node):
    
    def Evaluate(self, symbolTable):
        child = self.children[0].Evaluate(symbolTable)

        if self.value == "-":
            return -child
        if self.value == "+":
            return +child
        if self.value == "!":
            return not child
        raise ValueError("Invalid UnOp value")
            
class IntVal(Node):
    
    def Evaluate(self, symbolTable):
        return int(self.value)
        
class Identifier(Node):

    def Evaluate(self, symbolTable):
        return symbolTable.getSymbol(self.value)

      
class NoOp(Node):
    pass

class Print(Node):

    def Evaluate(self, symbolTable):
        child = self.children[0].Evaluate(symbolTable)

        print(child)
    
class Assignment(Node):
    
    def Evaluate(self, symbolTable):
        symbolTable.setSymbol(self.children[0].value, self.children[1].Evaluate(symbolTable))
    
class Conditional(Node):
    def Evaluate(self, symbolTable):
        conditional = self.children[0].Evaluate(symbolTable)

        if conditional:
            self.children[1].Evaluate(symbolTable)
        elif len(self.children) == 3:
            self.children[2].Evaluate(symbolTable)

class WhileLoop(Node):

    def Evaluate(self, symbolTable):
        conditional = self.children[0].Evaluate(symbolTable)
        while conditional:
            self.children[1].Evaluate(symbolTable)
            conditional = self.children[0].Evaluate(symbolTable)
    
class Input(Node):
    
    def Evaluate(self, symbolTable):
        return int(input())


    


    




    
            
# number1 = IntVal(1)
# number2 = IntVal(2)
# number3 = IntVal(5)
# unop = UnOp([number1], "-")
# operator2 = BinOp([number2, number3], "*")
# operator = BinOp([operator2, unop], "+")
# mainNode = Node([operator], None)

            

