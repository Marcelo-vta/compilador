import sys
from Parser import Parser
from utils import print_tree

if __name__ == "__main__":
    # input = sys.argv[1]
    # input = "3+6/3   *  2 -+-  +  2*4/2 + 0/1 -((6+ 4)/(2)) // Teste // Teste 2"

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            input = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

    parser = Parser()
    mainNode = parser.run(input)

    # print_tree(mainNode)

    print(mainNode.Evaluate())
