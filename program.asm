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
  mov eax, 1 ;
  neg eax ;
  push eax ;
  mov eax, 3 ;
  pop ecx ;
  add eax, ecx ;
  mov [EBP-4], eax ;
  mov eax, [EBP-4] ;
  mov [EBP-8], eax ;
  mov eax, 5 ;
  push eax ;
  mov eax, [EBP-4] ;
  pop ecx ;
  cmp eax, ecx ;
  mov ecx, 1 ;
  mov ecx, 0 ;
  cmovl eax, ecx ;
  push eax ;
  mov eax, 1 ;
  push eax ;
  mov eax, [EBP-4] ;
  pop ecx ;
  cmp eax, ecx ;
  mov ecx, 1 ;
  mov ecx, 0 ;
  cmovg eax, ecx ;
  pop ecx ;
  cmp eax, 0 ;
  setne al ;
  cmp ecx, 0 ;
  setne cl ;
  or al, cl ;
  movzx eax, al ;
  cmp eax, 0
  je exit_33
  mov eax, 1 ;
  push eax ;
  mov eax, 5 ;
  pop ecx ;
  sub eax, ecx ;
  mov [EBP-4], eax ;
  jmp exit_33
  exit_33:
  mov eax, 3 ;
  push eax ;
  mov eax, [EBP-8] ;
  pop ecx ;
  cmp eax, ecx ;
  mov ecx, 1 ;
  mov ecx, 0 ;
  cmove eax, ecx ;
  push eax ;
  mov eax, 3 ;
  push eax ;
  mov eax, [EBP-4] ;
  pop ecx ;
  cmp eax, ecx ;
  mov ecx, 1 ;
  mov ecx, 0 ;
  cmove eax, ecx ;
  pop ecx ;
  cmp eax, 0 ;
  setne al ;
  cmp ecx, 0 ;
  setne cl ;
  and al, cl ;
  movzx eax, al ;
  cmp eax, 0
  je else_48
  jmp exit_48
  else_48:
  mov eax, 3 ;
  mov [EBP-4], eax ;
  exit_48:
  mov eax, 3 ;
  mov [EBP-4], eax ;
  loop_70:
  mov eax, 5 ;
  push eax ;
  mov eax, [EBP-4] ;
  pop ecx ;
  cmp eax, ecx ;
  mov ecx, 1 ;
  mov ecx, 0 ;
  cmovl eax, ecx ;
  cmp eax, 0
  je exit_70
  mov eax, 1 ;
  push eax ;
  mov eax, [EBP-4] ;
  pop ecx ;
  sub eax, ecx ;
  mov [EBP-8], eax ;
  mov eax, 1 ;
  push eax ;
  mov eax, [EBP-4] ;
  pop ecx ;
  add eax, ecx ;
  mov [EBP-4], eax ;
  jmp loop_70
  exit_70:
  mov eax, [EBP-4] ;
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