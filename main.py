import sys
from Parser import Parser
from utils import print_tree
from SymbolTable import SymbolTable
from Code import Code

if __name__ == "__main__":
    # input = sys.argv[1]
    
    # input = """
    #     {
    #         var x: i32;
    #         var y: i32;
    #         x = 3+-1;
    #         y = x;
    #         if (x > 1 || x < 5) {
    #             x = 5-1;
    #         }
    #         if (x == 3 && y ==3) {
    #         }
    #         else {
    #             x = 3;
    #         }
    #         x = 3;
    #         while (x < 5) {
    #             y = x - 1;
    #             x = x + 1;
    #         }
    #         print(x);
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
    code = Code()
    # mainBlock.Evaluate(symbolTable)
    mainBlock.Generate(symbolTable, code)
    code.dump("program.asm")


