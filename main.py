import sys
from Parser import Parser

if __name__ == "__main__":
    input = sys.argv[1]
    # input = "1*2"
    parser = Parser()

    print(parser.run(input))
