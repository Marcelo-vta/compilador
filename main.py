import sys
from Parser import Parser

if __name__ == "__main__":
    # input = sys.argv[1]
    # input = "(1  -  2)*3"

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

    print(mainNode.Evaluate())