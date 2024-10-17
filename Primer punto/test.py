import sys
from antlr4 import *
from OperacionesComplLexer import OperacionesComplLexer
from OperacionesComplParser import OperacionesComplParser

# Clase para evaluar expresiones complejas
class ComplexEvaluator:

    def visit(self, ctx):
        # Lógica de evaluación de expresiones
        if ctx.ADDITION():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left + right
        elif ctx.SUBTRACTION():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left - right
        elif ctx.MULTIPLICATION():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left * right
        elif ctx.DIVISION():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left / right
        elif ctx.COMPLEX():
            return self.parse_complex(ctx.COMPLEX().getText())
        elif ctx.REAL():
            return complex(float(ctx.REAL().getText()), 0)
        
    def parse_complex(self, text):
        parts = text[:-1].split(' + ') if '+' in text else text[:-1].split(' - ')
        real = float(parts[0])
        imaginary = float(parts[1]) if '+' in text else -float(parts[1])
        return complex(real, imaginary)

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = OperacionesComplLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OperacionesComplParser(stream)
    tree = parser.expr()

    evaluator = ComplexEvaluator()
    result = evaluator.visit(tree)

    print("Resultado:", result)

if __name__ == '__main__':
    main()
