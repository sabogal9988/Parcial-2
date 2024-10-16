import sys
from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = MapFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapFilterParser(stream)
    tree = parser.statement()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
