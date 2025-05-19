class Code:
    instructions = []

    def append(self, code: str):
        self.instructions.append(code)
    
    def dump(self, filename):

        with open(filename, 'w') as file:
            file.write("""section .data
  format_out: db "%d", 10, 0 ;
  format_in: db "%d", 0 ;
  scan_int: dd 0 ;

section .text
  extern printf ;
  extern scanf ;
  global _start ;

_start:
  push ebp ;
  mov ebp, esp ;\n\n  """)

            file.write("\n  ".join(self.instructions))

            file.write("""\n
  mov esp, ebp ;
  pop ebp ;
  mov eax, 1 ;
  xor ebx, ebx ;
  int 0x80 ;""")