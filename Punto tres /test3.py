import sys
from antlr4 import *
from FourierTransformLexer import FourierTransformLexer
from FourierTransformParser import FourierTransformParser
import numpy as np

class FourierEvaluator:
    def visit(self, ctx):
        # Extraer la lista de expresiones
        values = self.extract_values(ctx.exprList)
        # Calcular la transformada de Fourier
        result = np.fft.fft(values)
        return result

    def extract_values(self, expr_list_ctx):
        values = []
        for expr in expr_list_ctx.expr:
            # Convertir cada expresión a un número flotante
            values.append(float(expr.getText()))
        return values

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = TransformadaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TransformadaParser(stream)
    tree = parser.statement()

    evaluator = FourierEvaluator()
    result = evaluator.visit(tree)

    print("Transformada de Fourier:", result)

if __name__ == '__main__':
    main()
