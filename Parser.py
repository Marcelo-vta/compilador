from Tokenizer import Tokenizer
from constants import SEQUENCE
from Node import *
from utils import print_tree


class Parser:
    tokenizer: Tokenizer

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
    
    def parseStatement(self, symbolTable):

        token = self.tokenizer.next
        if token.type == "identifier":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "equals":
                self.tokenizer.selectNext()
                expression = Node([self.parseExpression()], None)
                symbolTable.setSymbol(token.value, expression.Evaluate(symbolTable))
            else:
                raise SyntaxError("Set identifier like IDENTIFIER = VALUE")
            
        if token.type == "print":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type != "openPrio":
                raise SyntaxError("Unproper use of print, proper: print(<expression>)")
            self.tokenizer.selectNext()
            expression = Node([self.parseExpression()], None)
            if self.tokenizer.next.type != "closePrio":
                raise SyntaxError("Unproper use of print, proper: print(<expression>)")
            print(expression.Evaluate(symbolTable))
            self.tokenizer.selectNext()
        
        if self.tokenizer.next.type != "endStatement":
            raise SyntaxError("Unclosed statement")
        return

    def parseBlock(self, symbolTable):
        token = self.tokenizer.next
        if token.type != "openBlock":
            raise SyntaxError('Start block with "{"')
        
        self.tokenizer.selectNext()
        while self.tokenizer.next.type != "closeBlock":
            if self.tokenizer.next.value == "eof":
                raise SyntaxError("Unclosed block")
            self.parseStatement(symbolTable)
            self.tokenizer.selectNext()
        self.tokenizer.selectNext()
        return


    def run(self, code, symbolTable):
        self.tokenizer = Tokenizer(code)
        self.tokenizer.selectNext()
        self.parseBlock(symbolTable)

        if self.tokenizer.next.type != "eof":
            raise Exception("Unexpected end of input")

        return
