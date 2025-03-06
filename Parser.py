from Tokenizer import Tokenizer
from constants import SEQUENCE


class Parser:
    tokenizer: Tokenizer

    def parseFactor(self):
        token = self.tokenizer.next
        self.tokenizer.selectNext()

        right = None

        if token.value == "+":
            right = self.parseFactor()
        if token.value == "-":
            right = -self.parseFactor()

        if token.value == "(":
            right = self.parseExpression()
            if self.tokenizer.next.value != ")":
                raise Exception("Unclosed parenthesis")
            else:
                self.tokenizer.selectNext()

        if right == None:
            return int(token.value)
        return int(right)



    def parseTerm(self):
        value = self.parseFactor()

        while self.tokenizer.next.type == "operator" and self.tokenizer.next.value in ["*", "/"]:
            op = self.tokenizer.next.value
            self.tokenizer.selectNext()
            right = self.parseFactor()

            if op == "*":
                value *= right
            elif op == "/":
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                value = int(value/right)

        return value

    def parseExpression(self):
        value = self.parseTerm()

        while self.tokenizer.next.type == "operator" and self.tokenizer.next.value in ["+", "-"]:
            op = self.tokenizer.next.value
            self.tokenizer.selectNext()
            right = self.parseTerm()

            if op == "+":
                value += right
            elif op == "-":
                value -= right

        return value

    def run(self, code):
        self.tokenizer = Tokenizer(code)
        self.tokenizer.selectNext()
        result = self.parseExpression()

        if self.tokenizer.next.type != "eof":
            raise Exception("Unexpected end of input")

        return result
