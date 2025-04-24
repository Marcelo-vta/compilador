class Code:
    instructions = []

    def append(self, code: str):
        self.instructions.append(code)
    
    def dump(self, filename):

        with open(filename, 'w') as file:
            file.write("""section .data
  format_out: db "%d", 10, 0 ; format do printf
  format_in: db "%d", 0 ; format do scanf
  scan_int: dd 0; 32-bits integer`

section .text
  extern printf ; usar _printf para Windows
  extern scanf ; usar _scanf para Windows
  ; extern _ExitProcess@4 ; usar para Windows
  global _start ; início do programa

_start:
  push ebp ; guarda o EBP
  mov ebp, esp ; zera a pilha\n\n  """)

            file.write("\n  ".join(self.instructions))

            file.write("""\n
  mov esp, ebp ; reestabelece a pilha
  pop ebp

  ; chamada da interrupcao de saida (Linux)
  mov eax, 1   
  xor ebx, ebx 
  int 0x80""")