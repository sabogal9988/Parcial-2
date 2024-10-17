import sys
from antlr4 import *
from FourierTransformLexer import FourierTransformLexer
from FourierTransformParser import FourierTransformParser
import math

# Función recursiva para evaluar el árbol de sintaxis
def evaluate(ctx):
    if isinstance(ctx, FourierTransformParser.FourierTransformContext):
        exprs = evaluate(ctx.exprList())
        return f"Transformada de Fourier: {exprs}"
    
    elif isinstance(ctx, FourierTransformParser.InverseFourierTransformContext):
        exprs = evaluate(ctx.exprList())
        return f"Transformada Inversa de Fourier: {exprs}"
    
    elif isinstance(ctx, FourierTransformParser.ExprListContext):
        # Evaluar cada expresión en la lista de expresiones y unificar los resultados
        return ", ".join([evaluate(expr) for expr in ctx.expr()])
    
    elif isinstance(ctx, FourierTransformParser.RectContext):
        return "T*sinc(T*(w/2π))"
    
    elif isinstance(ctx, FourierTransformParser.TriContext):
        return "T*sinc^2(T*(w/2π))"
    
    elif isinstance(ctx, FourierTransformParser.CosContext):
        return "π*δ(w-w0) + π*δ(w+w0)"
    
    elif isinstance(ctx, FourierTransformParser.SinContext):
        return "(π/j)*δ(w-w0) - (π/j)*δ(w+w0)"
    
    elif isinstance(ctx, FourierTransformParser.DeltaContext):
        return "F[δ(t)]"
    
    elif isinstance(ctx, FourierTransformParser.IdentifierContext):
        return ctx.getText()
    
    elif isinstance(ctx, FourierTransformParser.RealContext):
        return ctx.getText()

# Función principal para leer la entrada y evaluar las expresiones
def calc(line) -> str:
    input_stream = InputStream(line)

    # Lexing
    lexer = FourierTransformLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Parsing
    parser = FourierTransformParser(stream)
    tree = parser.statement()  # Asumiendo que el punto de entrada de la gramática es 'statement'

    # Evaluar el árbol de forma recursiva
    return evaluate(tree)

if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input()
        if line.lower() == 'exit':
            break
        try:
            print(calc(line))
        except Exception as e:
            print("Error:", e)
