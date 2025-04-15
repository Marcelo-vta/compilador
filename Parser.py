from Tokenizer import Tokenizer
from constants import SEQUENCE
from Node import *
from utils import print_tree
from SymbolTable import *


class Parser:
    tokenizer: Tokenizer
    node: Node

    def parseFactor(self):
        token = self.tokenizer.next
        self.tokenizer.selectNext()

        node = None
        
        if token.value == "+":
            node = UnOp([self.parseFactor()], token)
        if token.value == "-":
            node = UnOp([self.parseFactor()], token)

        if token.value == "(":
            node = Node([self.parseExpression()], None)
            if self.tokenizer.next.value != ")":
                raise Exception("Unclosed parenthesis")
            else:
                self.tokenizer.selectNext()

        if token.value == "read":
            if self.tokenizer.next.value == "(":
                node = Input()
                self.tokenizer.selectNext()
            else:
                raise Exception("unexpected use of input")

            if self.tokenizer.next.value == ")":
                self.tokenizer.selectNext()
            else:
                raise Exception("Unclosed parenthesis")

        if node == None:
            if token.value.isnumeric():
                token.value = int(token.value) # arrumar isso dps, colocar int no Node.Evaluate()

            return IntVal(token)
        
        return node

    def parseTerm(self):
        node = self.parseFactor()

        while self.tokenizer.next.type == "operator" and self.tokenizer.next.value in ["*", "/"]:
            op = self.tokenizer.next
            self.tokenizer.selectNext()
            right = self.parseFactor()

            if op.value == "*":
                node = BinOp([node, right], op)
            elif op.value == "/":
                if right.value == 0:
                    raise ZeroDivisionError("Division by zero")
                node = BinOp([node, right], op)

        return node

    def parseExpression(self):
        node = self.parseTerm()

        while self.tokenizer.next.type == "operator" and self.tokenizer.next.value in ["+", "-"]:
            op = self.tokenizer.next
            self.tokenizer.selectNext()
            right = self.parseTerm()

            if op.value == "+":
                node = BinOp([node, right], op)
            elif op.value == "-":
                node = BinOp([node, right], op)

        return node
    
    def parseRelExp(self):
        node = self.parseExpression()

        while self.tokenizer.next.type in ["equals", "greaterThan", "lessThan", "greaterOrEqualsTo", "lessOrEqualsTo"]:
            op = self.tokenizer.next
            self.tokenizer.selectNext()
            right = self.parseExpression()

            node = BinOp([node, right], op)

        return node

    def parseBoolTerm(self):
        node = self.parseRelExp()
    
        while self.tokenizer.next.type == "and":
            op = self.tokenizer.next
            self.tokenizer.selectNext()
            right = self.parseRelExp()

            node = BinOp([node, right], op)

        return node
    
    def parseBoolExp(self):
        node = self.parseBoolTerm()

        while self.tokenizer.next.type == "or":
            op = self.tokenizer.next
            self.tokenizer.selectNext()
            right = self.parseBoolTerm()

            node = BinOp([node, right], op)

        return node

    def parseStatement(self):

        token = self.tokenizer.next
        node = Node([], None)

        if token.type == "identifier":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "equals":
                self.tokenizer.selectNext()
                node = Assignment([self.parseBoolExp()], token)
            else:
                raise SyntaxError("Set identifier like IDENTIFIER = VALUE")
            

        if token.type == "print":
            self.tokenizer.selectNext()

            if self.tokenizer.next.type != "openPrio":
                raise SyntaxError("Unproper use of print, proper: print(<expression>)")
            self.tokenizer.selectNext()

            node = Print([self.parseBoolExp()])

            if self.tokenizer.next.type != "closePrio":
                raise SyntaxError("Unproper use of print, proper: print(<expression>)")

            self.tokenizer.selectNext()


        if token.type == "if":
            self.tokenizer.selectNext()

            if self.tokenizer.next.type != "openPrio":
                raise SyntaxError("Unproper use of if, proper: if(<condition>){<block>}[else{<block>}]")
            self.tokenizer.selectNext()

            condition = self.parseBoolExp()

            if self.tokenizer.next.type != "closePrio":
                raise SyntaxError("Unproper use of if, proper: if(<condition>){<block>}[else{<block>}]")
            self.tokenizer.selectNext()
            
            onConditionTrue = self.parseBlock()

            conditionFalse = False
            if self.tokenizer.next.type == "else":
                conditionFalse = True
                onConditionFalse = self.parseBlock()
            
            if conditionFalse:
                node = Conditional([condition, onConditionTrue, onConditionFalse])
            else:
                node = Conditional([condition, onConditionTrue])

        
        if token.type == "while":
            self.tokenizer.selectNext()

            if self.tokenizer.next.type != "openPrio":
                raise SyntaxError("Unproper use of while, proper: while(<condition>){<block>}")
            self.tokenizer.selectNext()

            condition = self.parseBoolExp()

            if self.tokenizer.next.type != "closePrio":
                raise SyntaxError("Unproper use of while, proper: while(<condition>){<block>}")
            self.tokenizer.selectNext()

            content = self.parseBlock()

            node = WhileLoop([condition, content])

        if self.tokenizer.next.type != "endStatement":
            raise SyntaxError("Unclosed statement")
        
        self.tokenizer.selectNext()
        return node

    def parseBlock(self):
        statements = []

        token = self.tokenizer.next
        if token.type != "openBlock":
            raise SyntaxError('Start block with "{"')
        
        self.tokenizer.selectNext()
        while self.tokenizer.next.type != "closeBlock":
            if self.tokenizer.next.value == "eof":
                raise SyntaxError("Unclosed block")
            statements.append(self.parseStatement())    
        self.tokenizer.selectNext()

        return Block(statements)


    def run(self, code):
        self.tokenizer = Tokenizer(code)
        self.tokenizer.selectNext()

        symbolTable = SymbolTable()

        mainBlock = self.parseBlock()
        mainBlock.Evaluate(symbolTable)

        if self.tokenizer.next.type != "eof":
            raise Exception("Unexpected end of input")

        return
