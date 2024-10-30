from antlr4 import *
from FourierTransformLexer import FourierTransformLexer
from FourierTransformParser import FourierTransformParser
from FourierTransformVisitor import FourierTransformVisitor


# Visitante personalizado para evaluar transformadas de Fourier
class FourierVisitor(FourierTransformVisitor):

    def visitFourierTransform(self, ctx):
        exprs = self.visit(ctx.exprList())
        return f"Transformada de Fourier: {exprs}"

    def visitInverseFourierTransform(self, ctx):
        exprs = self.visit(ctx.exprList())
        return f"Transformada Inversa de Fourier: {exprs}"

    def visitExprList(self, ctx):
        return ", ".join([self.visit(expr) for expr in ctx.expr()])

    # Métodos para evaluar las funciones específicas
    def visitRect(self, ctx):
        return "T*sinc(T*(w/2π))"

    def visitTri(self, ctx):
        return "T*sinc^2(T*(w/2π))"

    def visitCos(self, ctx):
        return "π*δ(w-w0) + π*δ(w+w0)"

    def visitSin(self, ctx):
        return "(π/j)*δ(w-w0) - (π/j)*δ(w+w0)"

    def visitDelta(self, ctx):
        return "F[δ(t)]"

    def visitExprIdentifier(self, ctx):
        return ctx.getText()

    def visitExprReal(self, ctx):
        return ctx.getText()


# Función principal para leer la entrada y evaluar las expresiones
def calc(line) -> str:
    input_stream = InputStream(line)

    # Tokenización
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
        try:
            line = input("Ingrese una expresión: ")
            if not line:
                break
            result = calc(line)
            print("Resultado:", result)
        except Exception as e:
            print(f"Error: {e}")
