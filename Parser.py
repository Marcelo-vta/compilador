from Tokenizer import Tokenizer
from constants import SEQUENCE
from Node import *


class Parser:
    tokenizer: Tokenizer

    def parseFactor(self):
        token = self.tokenizer.next
        self.tokenizer.selectNext()

        node = None
        
        if token.value == "+":
            node = UnOp([self.parseFactor()], "+")
        if token.value == "-":
            node = UnOp([self.parseFactor()], "-")

        if token.value == "(":
            node = Node([self.parseExpression()], None)
            if self.tokenizer.next.value != ")":
                raise Exception("Unclosed parenthesis")
            else:
                self.tokenizer.selectNext()

        if node == None:
            return IntVal(int(token.value))
        return node



    def parseTerm(self):
        node = self.parseFactor()

        if self.tokenizer.next.type == "operator" and self.tokenizer.next.value in ["*", "/"]:
            op = self.tokenizer.next.value
            self.tokenizer.selectNext()
            right = self.parseExpression()

            if op == "*":
                node = BinOp([node, right], "*")
            elif op == "/":
                if right.value == 0:
                    raise ZeroDivisionError("Division by zero")
                node = BinOp([node, right], "/")

        return node

    def parseExpression(self):
        node = self.parseTerm()

        if self.tokenizer.next.type == "operator" and self.tokenizer.next.value in ["+", "-"]:
            op = self.tokenizer.next.value
            self.tokenizer.selectNext()
            right = self.parseExpression()

            if op == "+":
                node = BinOp([node, right], "+")
            elif op == "-":
                node = BinOp([node, right], "-")

        return node

    def run(self, code):
        self.tokenizer = Tokenizer(code)
        self.tokenizer.selectNext()
        mainNode = Node([self.parseExpression()],None)

        if self.tokenizer.next.type != "eof":
            raise Exception("Unexpected end of input")

        return mainNode
