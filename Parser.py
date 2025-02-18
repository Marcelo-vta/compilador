from Tokenizer import Tokenizer
from constants import SEQUENCE

class Parser():
    tokenizer: Tokenizer


    def parseExpression(self, total=0):
        last_token = self.tokenizer.next

        self.tokenizer.selectNext()
        if self.tokenizer.next.type not in SEQUENCE[last_token.type]:
            raise Exception

        if last_token.type in ["", "operator"]:
            if last_token.value in ["", "+"]:
                total += int(self.tokenizer.next.value)
            else:
                total -= int(self.tokenizer.next.value)

        if self.tokenizer.next.type == "eof":
            return total

        return self.parseExpression(total)
      

    def run(self, code):
        self.tokenizer = Tokenizer(code)
        return self.parseExpression()
            




