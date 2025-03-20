

class Node():
    children:list['Node']

    def __init__(self, children, value):
        self.children = children
        self.value = value
        return
    
    def Evaluate(self):
        for i in range(len(self.children)):
            self.children[i] = self.children[i].Evaluate()

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
        
    def Evaluate(self):
        super().Evaluate()
        match self.value:
            case "-":
                return self.children[0] - self.children[1]
            case "+":
                return self.children[0] + self.children[1]
            case "*":
                return self.children[0] * self.children[1]
            case "/":
                return self.children[0] // self.children[1]
            case _:
                raise ValueError("Invalid BinOp value")

class UnOp(Node):
    def __init__(self, children, value):
        super().__init__(children, value)

        if len(children) != 1:
            raise ValueError("UnOp contains one children")
        return
    
    def Evaluate(self):
        super().Evaluate()
        match self.value:
            case "-":
                return -(self.children[0])
            case "+":
                return self.children[0]
            case _:
                raise ValueError("Invalid UnOp value")
            
class IntVal(Node):
    def __init__(self, value):
        super().__init__([], value)
    
    def Evaluate(self):
        super().Evaluate()

        if isinstance(self.value, int):
            return self.value
        else:
            raise ValueError("IntVal value must be an integer")
        
class NoOp(Node):
    def __init__(self, value):
        super().__init__([], value)

    def Evaluate(self):
        super().Evaluate()

        return self.value

            
# number1 = IntVal(1)
# number2 = IntVal(2)
# number3 = IntVal(5)
# unop = UnOp([number1], "-")
# operator2 = BinOp([number2, number3], "*")
# operator = BinOp([operator2, unop], "+")
# mainNode = Node([operator], None)

            

