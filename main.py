import sys
from Parser import Parser
from utils import print_tree
from SymbolTable import SymbolTable

if __name__ == "__main__":
    # input = sys.argv[1]
    
    # input = """
    #     fn soma(x: i32, y: i32) i32 {
    #         var a: i32;
    #         a = x + y;
    #         print(a);
    #         return a;
    #     }
    #     fn main() i32 {
    #         var a: i32;
    #         var b: i32;
    #         a = 3;
    #         b = soma(a, 4);
    #         print(a);
    #         print(b);
    #     }
    # """

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
    print("deubom :)")
    mainBlock.Evaluate(symbolTable)


