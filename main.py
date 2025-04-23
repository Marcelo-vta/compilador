import sys
from Parser import Parser
from utils import print_tree
from SymbolTable import SymbolTable

if __name__ == "__main__":
    # input = sys.argv[1]
    input = """
        {
            x_1 = reader();
            
            if ((x_1 > 1 && !(x_1 < 1)) || x_1 == 3){x_1 = 2;}      
            print(x_1);

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

    parser.run(input)

