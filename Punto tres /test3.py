import sys
from antlr4 import *
from FourierTransformLexer import FourierTransformLexer
from FourierTransformParser import FourierTransformParser

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = FourierTransformLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FourierTransformParser(stream)
    tree = parser.statement()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
