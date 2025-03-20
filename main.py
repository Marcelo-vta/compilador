import sys
from Parser import Parser
from utils import print_tree
from SymbolTable import SymbolTable

if __name__ == "__main__":
    # input = sys.argv[1]
    # input = "{x1 = 3; y2 = 4; z_final = x1 + y2; print(z_final);}"

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            input = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

    parser = Parser()
    symbolTable = SymbolTable()

    parser.run(input, symbolTable)

