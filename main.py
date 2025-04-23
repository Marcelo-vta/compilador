import sys
from Parser import Parser
from utils import print_tree
from SymbolTable import SymbolTable

if __name__ == "__main__":
    # input = sys.argv[1]
    input = """
        {
            x_1 = reader();
            
            print(x_1);
            
            if ((x_1 > 1 && !(x_1 < 1)) || x_1 == 3) {
                x_1 = 2;
            }
            
            x = 3+6/3   *  2 -+-  +  2*4/2 + 0/1 -((6+ ((4)))/(2)); // Teste // Teste 2
            y_1 = 3;
            y_1 = y_1 + x_1;
            z__ = x + y_1;
            
            if (x_1 == 2) {
                x_1 = 2;
            }
            
            if (x_1 == 3) {
                x_1 = 2;
            } else {
                x_1 = 3;
            }
            
            x_1 = 0;
            while (x_1 < 1 || x == 2) {
                print(x_1);
                x_1 = x_1 + 1;
            } 
            ;;;
            
            
            // Saida final;
            print(x_1);
            print(x);
            print(z__+1);
            
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
    mainBlock.Evaluate(symbolTable)


