import sys
from Parser import Parser

if __name__ == "__main__":
    input = sys.argv[1]
    # input = "3+6/3   *  2 -+-  +  2*4/2 + 0/1 -((6+ ((4)))/(2))"
    parser = Parser()

    print(parser.run(input))
