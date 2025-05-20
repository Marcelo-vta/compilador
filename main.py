import sys
from Parser import Parser
from utils import print_tree
from SymbolTable import SymbolTable

if __name__ == "__main__":
    # input = sys.argv[1]
    
#     input = """

# fn fac(x: i32) i32 {
#   if (x == 1) {
#     return 1;
#   }
#   return x * fac(x-1);
# }

# fn main() void {
#   var x_1:i32;
#   x_1 = reader();
#   var x_2:i32 = fac(4); 
#   ;;;
# }
#     """

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            input = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

    parser = Parser()
    mainBlock = parser.run(input)

    symbolTable = SymbolTable()
    # print("deubom :)")
    mainBlock.Evaluate(symbolTable)


