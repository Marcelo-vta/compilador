from Token import Token
from constants import VOCABULARY
from PrePro import PrePro

class Tokenizer():
    source: str
    position: int
    next: Token

    def __init__(self, source):
        prePro = PrePro()
        self.source = prePro.filter(source)
        self.position = 0
        self.next = Token()

    def selectNext(self):

        newToken = Token()

        if self.position >= len(self.source):
            newToken.type = "eof"
            newToken.value = "eof"
            self.next = newToken
            return

        c_char = self.source[self.position]

        if c_char not in VOCABULARY:
            newToken.type = "Unexpected Token"
            newToken.value = c_char
            self.next = newToken
            self.position += 1
            return

        while c_char.isnumeric():
            newToken.type = "number"
            newToken.value += c_char
            self.position += 1
            if self.position >= len(self.source):
                self.next = newToken
                return
            c_char = self.source[self.position]
            if not c_char.isnumeric():
                self.next = newToken
                return
            
        if c_char in ["+", "-", "*", "/"]:
            newToken.type = "operator"
            newToken.value = c_char
            self.next = newToken
            self.position += 1
            return
        
        if c_char == "(":
            newToken.type = "openPrio"
            newToken.value = c_char
            self.next = newToken
            self.position += 1
            return
        
        if c_char == ")":
            newToken.type = "closePrio"
            newToken.value = c_char
            self.next = newToken
            self.position += 1
            return
        
        if c_char == "{":
            newToken.type = "openBlock"
            newToken.value = c_char
            self.next = newToken
            self.position += 1
            return
        
        if c_char == "}":
            newToken.type = "closeBlock"
            newToken.value = c_char
            self.next = newToken
            self.position += 1
            return
        

        if c_char.isalpha() or c_char == "_":
            newToken.type = "identifier"
            newToken.value = ""
            while c_char.isalnum() or c_char == "_":
                newToken.value += c_char
                self.position += 1
                if self.position >= len(self.source):
                    self.next = newToken
                    return
                c_char = self.source[self.position]
                if not (c_char.isalnum() or c_char == '_'):
                    if newToken.value == "print":
                        newToken.type = "print"
                    self.next = newToken
                    return
            
        if c_char == "=":
            newToken.type = "equals"
            newToken.value = c_char
            self.next = newToken
            self.position += 1
            return
        
        if c_char == ";":
            newToken.type = "endStatement"
            newToken.value = c_char
            self.next = newToken
            self.position += 1
            return
        
        self.position += 1        
        self.selectNext()


# tkn = Tokenizer("teste 3 + 2 testando1 print {};")
# for i in range(20):
#     print(tkn.next.type)
#     tkn.selectNext()
