from antlr4 import *
from FourierTransformLexer import FourierTransformLexer
from FourierTransformParser import FourierTransformParser
from FourierTransformVisitor import FourierTransformVisitor
import math

# Visitante personalizado para evaluar transformadas de Fourier
class FourierVisitor(FourierTransformVisitor):
    
    def visitFourierTransform(self, ctx:FourierTransformParser.FourierTransformContext):
        exprs = self.visit(ctx.exprList())
# Función recursiva para evaluar el árbol de sintaxis
def evaluate(ctx):
    if isinstance(ctx, FourierTransformParser.FourierTransformContext):
        exprs = evaluate(ctx.exprList())
return f"Transformada de Fourier: {exprs}"

    def visitInverseFourierTransform(self, ctx:FourierTransformParser.InverseFourierTransformContext):
        exprs = self.visit(ctx.exprList())
    elif isinstance(ctx, FourierTransformParser.InverseFourierTransformContext):
        exprs = evaluate(ctx.exprList())
return f"Transformada Inversa de Fourier: {exprs}"

    def visitExprList(self, ctx:FourierTransformParser.ExprListContext):
    elif isinstance(ctx, FourierTransformParser.ExprListContext):
# Evaluar cada expresión en la lista de expresiones y unificar los resultados
        return ", ".join([self.visit(expr) for expr in ctx.expr()])

    # Métodos para evaluar las funciones específicas
    def visitRect(self, ctx:FourierTransformParser.RectContext):
        return ", ".join([evaluate(expr) for expr in ctx.expr()])
    
    elif isinstance(ctx, FourierTransformParser.RectContext):
return "T*sinc(T*(w/2π))"

    def visitTri(self, ctx:FourierTransformParser.TriContext):
    elif isinstance(ctx, FourierTransformParser.TriContext):
return "T*sinc^2(T*(w/2π))"

    def visitCos(self, ctx:FourierTransformParser.CosContext):
    elif isinstance(ctx, FourierTransformParser.CosContext):
return "π*δ(w-w0) + π*δ(w+w0)"

    def visitSin(self, ctx:FourierTransformParser.SinContext):
    elif isinstance(ctx, FourierTransformParser.SinContext):
return "(π/j)*δ(w-w0) - (π/j)*δ(w+w0)"

    def visitDelta(self, ctx:FourierTransformParser.DeltaContext):
    elif isinstance(ctx, FourierTransformParser.DeltaContext):
return "F[δ(t)]"

    def visitIdentifier(self, ctx:FourierTransformParser.IdentifierContext):
    elif isinstance(ctx, FourierTransformParser.IdentifierContext):
return ctx.getText()

    def visitReal(self, ctx:FourierTransformParser.RealContext):
    
    elif isinstance(ctx, FourierTransformParser.RealContext):
return ctx.getText()

# Función principal para leer la entrada y evaluar las expresiones
def calc(line) -> str:
input_stream = InputStream(line)

@@ -51,11 +49,10 @@ def calc(line) -> str:

# Parsing
parser = FourierTransformParser(stream)
    tree = parser.statement()
    tree = parser.statement()  # Asumiendo que el punto de entrada de la gramática es 'statement'

    # Utilizar el visitante personalizado para recorrer el AST
    visitor = FourierVisitor()
    return visitor.visit(tree)
    # Evaluar el árbol de forma recursiva
    return evaluate(tree)

if __name__ == '__main__':
while True:
