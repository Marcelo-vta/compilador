section .data
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
  mov ebp, esp ; zera a pilha

  sub ESP, 4 ;
  sub ESP, 4 ;
  sub ESP, 4 ;
  mov eax, 1 ;
  mov [EBP-12], eax ;
  push scan_int ;
  push format_in ;
  call scanf ;
  add esp, 8 ;
  mov eax, dword [scan_int] ;
  mov [EBP-8], eax ;
  mov eax, 2 ;
  mov [EBP-4], eax ;
  loop_38:
  mov eax, 1 ;
  push eax ;
  mov eax, [EBP-8] ;
  pop ecx ;
  add eax, ecx ;
  push eax ;
  mov eax, [EBP-4] ;
  pop ecx ;
  cmp eax, ecx ;
  mov ecx, 1 ;
  mov ecx, 0 ;
  cmovl eax, ecx ;
  cmp eax, 0
  je exit_38
  mov eax, [EBP-4] ;
  push eax ;
  mov eax, [EBP-12] ;
  pop ecx ;
  imul eax, ecx ;
  mov [EBP-12], eax ;
  mov eax, 1 ;
  push eax ;
  mov eax, [EBP-4] ;
  pop ecx ;
  add eax, ecx ;
  mov [EBP-4], eax ;
  jmp loop_38
  exit_38:
  mov eax, [EBP-12] ;
  push eax ;
  push format_out ;
  call printf ;
  add esp, 8 ;

  mov esp, ebp ; reestabelece a pilha
  pop ebp

  ; chamada da interrupcao de saida (Linux)
  mov eax, 1   
  xor ebx, ebx 
  int 0x80