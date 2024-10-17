import sys
from antlr4 import *
from FourierTransformLexer import FourierTransformLexer
from FourierTransformParser import FourierTransformParser
from FourierTransformVisitor import FourierTransformVisitor
import math

# Visitante personalizado para evaluar transformadas de Fourier
class FourierVisitor(FourierTransformVisitor):
    
    def visitFourierTransform(self, ctx:FourierTransformParser.FourierTransformContext):
        exprs = self.visit(ctx.exprList())
        return f"Transformada de Fourier: {exprs}"
    
    def visitInverseFourierTransform(self, ctx:FourierTransformParser.InverseFourierTransformContext):
        exprs = self.visit(ctx.exprList())
        return f"Transformada Inversa de Fourier: {exprs}"
    
    def visitExprList(self, ctx:FourierTransformParser.ExprListContext):
        # Evaluar cada expresión en la lista de expresiones y unificar los resultados
        return ", ".join([self.visit(expr) for expr in ctx.expr()])

    # Métodos para evaluar las funciones específicas
    def visitRect(self, ctx:FourierTransformParser.RectContext):
        return "T*sinc(T*(w/2π))"
    
    def visitTri(self, ctx:FourierTransformParser.TriContext):
        return "T*sinc^2(T*(w/2π))"
    
    def visitCos(self, ctx:FourierTransformParser.CosContext):
        return "π*δ(w-w0) + π*δ(w+w0)"
    
    def visitSin(self, ctx:FourierTransformParser.SinContext):
        return "(π/j)*δ(w-w0) - (π/j)*δ(w+w0)"
    
    def visitDelta(self, ctx:FourierTransformParser.DeltaContext):
        return "F[δ(t)]"
    
    def visitIdentifier(self, ctx:FourierTransformParser.IdentifierContext):
        return ctx.getText()

    def visitReal(self, ctx:FourierTransformParser.RealContext):
        return ctx.getText()

def calc(line) -> str:
    input_stream = InputStream(line)

    # Lexing
    lexer = FourierTransformLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Parsing
    parser = FourierTransformParser(stream)
    tree = parser.statement()

    # Utilizar el visitante personalizado para recorrer el AST
    visitor = FourierVisitor()
    return visitor.visit(tree)

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
