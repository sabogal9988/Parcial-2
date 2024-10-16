import sys
from antlr4 import *
from ComplexOperationsLexer import ComplexOperationsLexer
from ComplexOperationsParser import ComplexOperationsParser

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = ComplexOperationsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplexOperationsParser(stream)
    tree = parser.expr()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
