import sys
from Parser import Parser
from utils import print_tree
from SymbolTable import SymbolTable
from Code import Code

if __name__ == "__main__":
    # input = sys.argv[1]
    
    input = """
        {
            var i: i32;
            var n: i32;
            var f: i32 = 1;
            n = reader();
            i = 2;
            while (i < n + 1) {
            f = f * i;
            i = i + 1;
            }
            print(f);
        }
    """

    # filename = sys.argv[1]

    # try:
    #     with open(filename, 'r', encoding='utf-8') as file:
    #         input = file.read()
    # except FileNotFoundError:
    #     print(f"Erro: Arquivo '{filename}' não encontrado.")
    # except Exception as e:
    #     print(f"Erro ao abrir o arquivo: {e}")

    parser = Parser()
    mainBlock = parser.run(input)

    symbolTable = SymbolTable()
    code = Code()


    # mainBlock.Evaluate(symbolTable)
    mainBlock.Generate(symbolTable, code)
    code.dump(f".asm")


