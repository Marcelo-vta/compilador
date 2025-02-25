from Tokenizer import Tokenizer
from constants import SEQUENCE


class Parser:
    tokenizer: Tokenizer

    def parseTerm(self):
        last_token = self.tokenizer.next
        self.tokenizer.selectNext()

        if self.tokenizer.next.type not in SEQUENCE.get(last_token.type, []):
            raise Exception("Unexpected token sequence")

        if self.tokenizer.next.type == "operator":
            if self.tokenizer.next.value in ["*", "/"]:
                op = self.tokenizer.next.value
                self.tokenizer.selectNext()
                right = self.parseTerm()

                if op == "*":
                    return int(int(last_token.value) * right)
                elif op == "/":
                    if right == 0:
                        raise ZeroDivisionError("Division by zero")
                    return int(int(last_token.value) / right)

        if self.tokenizer.next.type == "eof":
            return int(last_token.value)

        return int(last_token.value)

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

