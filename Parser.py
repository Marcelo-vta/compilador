from Tokenizer import Tokenizer
from constants import SEQUENCE


class Parser():
    tokenizer: Tokenizer

    def parseTerm(self):
        last_token = self.tokenizer.next

        self.tokenizer.selectNext()
        if self.tokenizer.next.type not in SEQUENCE[last_token.type]:
            raise Exception
        
        if self.tokenizer.next.type == "operator":
            if self.tokenizer.next.value in ["*", "/"]:
                if self.tokenizer.next.value == "*":
                    return int(int(last_token.value) * self.parseTerm())
                else:
                    return int(int(last_token.value) / self.parseTerm())
            else:
                return int(last_token.value)
        
        if self.tokenizer.next.type == "eof":
            return int(last_token.value)

        return self.parseTerm()

    def parseExpression(self):
        last_token = self.tokenizer.next
        if last_token.type == "eof":
            return 0
        
        value = self.parseTerm()

        if last_token.type in ["", "operator"]:
            if last_token.value in ["", "+"]:
                return value + self.parseExpression()
            elif last_token.value == "-":
                return value - self.parseExpression()

        if self.tokenizer.next.type == "eof":
            return value

    def run(self, code):
        self.tokenizer = Tokenizer(code)
        return self.parseExpression()
    
# teste = Parser()
# print(teste.run("1+6/2"))
