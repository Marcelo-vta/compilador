import sys
from Parser import Parser
from utils import print_tree
from SymbolTable import SymbolTable

if __name__ == "__main__":
    # input = sys.argv[1]
    
    # input = """
    #     {
    #         var x_1 : str = "teste" ++ " ta;
    #         print(x_1);
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
    mainBlock.Evaluate(symbolTable)


