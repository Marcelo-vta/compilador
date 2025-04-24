from var import Var

class Node():

    id = 0

    def generate_id():
        Node.id += 1
        return Node.id

    def __init__(self, children, value):
        self.children = children
        self.value = value
        self.id = Node.generate_id()
    
    def Evaluate(self, symbolTable):
        pass

    def Generate(self, symbolTable, code):
        pass

        
class Block(Node):
    def Evaluate(self, symbolTable):
        for child in self.children:
            child.Evaluate(symbolTable)

    def Generate(self, symbolTable, code):
        for child in self.children:
            child.Generate(symbolTable, code)
    
class BinOp(Node):
        
    def Evaluate(self, symbolTable):

        left = self.children[0].Evaluate(symbolTable)
        right = self.children[1].Evaluate(symbolTable)

        if left.type == "i32" and right.type == "i32":
            if self.value == "-":
                return Var("i32", left.value - right.value)
            if self.value == "+":
                return Var("i32", left.value + right.value)
            if self.value == "*":
                return Var("i32", left.value * right.value)
            if self.value == "/":
                return Var("i32", left.value // right.value)        
            
        if left.type == "bool" and right.type == "bool":
            if self.value == "||":
                return Var("bool", left.value or right.value)
            if self.value == "&&":
                return Var("bool", left.value and right.value)
        
        if left.type == right.type:
            if self.value == "==":
                return Var("bool", left.value == right.value)
            if self.value == ">=":
                return Var("bool", left.value >= right.value)
            if self.value == "<=":
                return Var("bool", left.value <= right.value)
            if self.value == "<":
                return Var("bool", left.value < right.value)
            if self.value == ">":
                return Var("bool", left.value > right.value)
        
        if self.value == "++":
            if left.type == "bool":
                left.value = str(left.value).lower()
            if right.type == "bool":
                right.value = str(right.value).lower()
            
            return Var("str", str(left.value) + str(right.value))
        
        raise Exception(f"unsupported type {left.type} or {right.type} for operand {self.value}")
    
    def Generate(self, symbolTable, code):
        self.children[1].Generate(symbolTable, code)
        code.append(
            "push eax ;"
        )
        self.children[0].Generate(symbolTable, code)
        code.append("pop ecx ;")

        if self.value == "-":
            code.append("sub eax, ecx ;")
        elif self.value == "+":
            code.append("add eax, ecx ;")
        elif self.value == "*":
            code.append("imul ecx ;")
        elif self.value == "/":
            code.append("cqo")
            code.append("idiv ecx ;")          
        elif self.value == "||":
            code.append("cmp eax, 0")
            code.append("mov eax, 0")
            code.append("mov edx, 1")
            code.append("cmovne eax, edx")
            code.append("cmp ecx, 0")
            code.append("mov ecx, 0")
            code.append("mov edx, 1")
            code.append("cmovne ecx, edx")
            code.append("or eax, ecx")

        elif self.value == "&&":
            code.append("cmp eax, 0")
            code.append("mov eax, 0")
            code.append("mov edx, 1")
            code.append("cmovne eax, edx") 
            code.append("cmp ecx, 0")
            code.append("mov ecx, 0")
            code.append("mov edx, 1")
            code.append("cmovne ecx, edx")
            code.append("and eax, ecx")
        

        elif self.value == "==":
            code.append("cmp eax, ecx ;")
            code.append("mov ecx, 1 ;")
            code.append("mov ecx, 0 ;")
            code.append("cmove eax, ecx ;")

        elif self.value == "<":
            code.append("cmp eax, ecx ;")
            code.append("mov ecx, 1 ;")
            code.append("mov ecx, 0 ;")
            code.append("cmovl eax, ecx ;")
            
        elif self.value == ">":
            code.append("cmp eax, ecx ;")
            code.append("mov ecx, 1 ;")
            code.append("mov ecx, 0 ;")
            code.append("cmovg eax, ecx ;")
            
        
        else:
            raise Exception(f"unsupported type")


        
        


class UnOp(Node):
    
    def Evaluate(self, symbolTable):
        child = self.children[0].Evaluate(symbolTable)

        if child.type == "i32":
            if self.value == "-":
                return Var("i32", -child.value)
            if self.value == "+":
                return Var("i32", +child.value)
        
        if child.type == "bool":        
            if self.value == "!":
                return Var("bool", not child.value)
        
        raise ValueError(f"unsupported type {child.type} for operand {self.value}")
    
    def Generate(self, symbolTable, code):

        self.children[0].Generate(symbolTable, code)

        if self.value == "-":
            code.append("neg eax ;")   

        elif self.value == "!":
            code.appeend("cmp eax, 0")
            code.appeend("mov eax, 0")
            code.appeend("mov ecx, 1")
            code.appeend("cmove eax, ecx")
        
        else:
            raise ValueError(f"unsupported type for operand {self.value}")

    
            
class IntVal(Node):
    
    def Evaluate(self, symbolTable):
        return Var('i32' , int(self.value))
    
    def Generate(self,  symbolTable, code):
        code.append(f"mov eax, {self.value} ;")
        
class BoolVal(Node):
    
    def Evaluate(self, symbolTable):
        return Var('bool', self.value == "true")
    
class StrVal(Node):
    
    def Evaluate(self, symbolTable):
        return Var('str' ,self.value)
    
        
class Identifier(Node):

    def Evaluate(self, symbolTable):
        return symbolTable.getSymbol(self.value)
    def Generate(self, symbolTable, code):
        code.append(f"mov eax, {symbolTable.getShift(self.value)} ;")

    
class VarDec(Node):

    def Evaluate(self, symbolTable):

        id = self.children[0].value
        type = self.value

        if len(self.children) > 1:
            value = self.children[1].Evaluate(symbolTable)
        else:
            if type == "i32":
                value = Var("i32", 0)
            if type == "str":
                value = Var("str", "")
            if type == "bool":
                value = Var("bool", False)

        if type != value.type:
            raise Exception("Unexpected type")
        
        symbolTable.setSymbol(id, Var(type, value.value))

    def Generate(self, symbolTable, code):

        id = self.children[0].value
        symbolTable.setSymbol(id)

        code.append("sub ESP, 4 ;")

        if len(self.children) > 1:
            self.children[1].Generate(symbolTable, code)

            code.append(f"mov {symbolTable.getShift(id)}, eax ;")

        



class Assignment(Node):
    
    def Evaluate(self, symbolTable):
        id = self.children[0].value
        value = self.children[1].Evaluate(symbolTable)

        try:
            symbolTable.getSymbol(id)
        except:
            raise Exception(f"Variable {id} not declaired")

        symbolTable.setSymbolValue(id, value.value)

    def Generate(self, symbolTable, code):

        id = self.children[0].value
        self.children[1].Generate(symbolTable, code)

        code.append(f"mov {symbolTable.getShift(id)}, eax ;")
        

      
class NoOp(Node):
    pass

class Print(Node):

    def Evaluate(self, symbolTable):
        child = self.children[0].Evaluate(symbolTable)

        if child.type == "bool":
            child.value = str(child.value).lower()

        print(child.value)

    def Generate(self, symbolTable, code):
        self.children[0].Generate(symbolTable, code)

        code.append("push eax ;")
        code.append("push format_out ;")
        code.append("call printf ;")
        code.append("add esp, 8 ;")
    
    
class Conditional(Node):
    def Evaluate(self, symbolTable):
        conditional = self.children[0].Evaluate(symbolTable)
        if conditional.type != "bool":
            raise Exception("Incompatible types")

        if conditional.value:
            self.children[1].Evaluate(symbolTable)
        elif len(self.children) == 3:
            self.children[2].Evaluate(symbolTable)
    
    def Generate(self, symbolTable, code):
        self.children[0].Generate(symbolTable, code)

        code.append("cmp eax, 0")
        if len(self.children) == 3:
            code.append(f"je else_{self.id}")
        else:
            code.append(f"je exit_{self.id}")
        
        self.children[1].Generate(symbolTable, code)
        code.append(f"jmp exit_{self.id}")
        
        if len(self.children) == 3:
            code.append(f"else_{self.id}:")
            self.children[2].Generate(symbolTable, code)
        
        code.append(f"exit_{self.id}:")


class WhileLoop(Node):

    def Evaluate(self, symbolTable):
        conditional = self.children[0].Evaluate(symbolTable)
        if conditional.type != "bool":
            raise Exception("Incompatible types")

        while conditional.value:
            self.children[1].Evaluate(symbolTable)
            conditional = self.children[0].Evaluate(symbolTable)

    def Generate(self, symbolTable, code):
        code.append(f"loop_{self.id}:")

        self.children[0].Generate(symbolTable, code)

        code.append("cmp eax, 0")
        code.append(f"je exit_{self.id}")

        self.children[1].Generate(symbolTable, code)

        code.append(f"jmp loop_{self.id}")
        code.append(f"exit_{self.id}:")


    
class Input(Node):
    
    def Evaluate(self, symbolTable):
        return Var("i32", int(input()))
    
    def Generate(self, symbolTable, code):
        code.append("push scan_int ;")
        code.append("push format_in ;")
        code.append("call scanf ;")
        code.append("add esp, 8 ;")
        code.append("mov eax, dword [scan_int] ;")


    


    




    
            
# number1 = IntVal(1)
# number2 = IntVal(2)
# number3 = IntVal(5)
# unop = UnOp([number1], "-")
# operator2 = BinOp([number2, number3], "*")
# operator = BinOp([operator2, unop], "+")
# mainNode = Node([operator], None)

            

