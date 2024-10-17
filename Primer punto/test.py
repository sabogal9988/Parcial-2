import sys
from antlr4 import *
from dist.OperacionesComplLexer import OperacionesComplLexer
from dist.OperacionesComplParser import OperacionesComplParser
from dist.OperacionesComplVisitor import OperacionesComplVisitor
import cmath

# Clase que hereda del visitante generado por ANTLR y evalúa expresiones
class ComplexVisitor(OperacionesComplVisitor):
    def visitAddSubExpr(self, ctx: OperacionesComplParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def visitMulDivExpr(self, ctx: OperacionesComplParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                print("¡División por cero!")
                return 0
            return left / right

    def visitAtomExpr(self, ctx: OperacionesComplParser.AtomExprContext):
        if 'i' in ctx.getText():  # Check if the atom is imaginary
            return complex(ctx.getText().replace('i', 'j'))  # Replace 'i' with 'j' for Python's complex numbers
        else:
            return complex(float(ctx.getText()), 0)

    def visitParenExpr(self, ctx: OperacionesComplParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitComparisonExpr(self, ctx: OperacionesComplParser.ComparisonExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '>':
            return left > right
        elif op == '>=':
            return left >= right
        elif op == '<':
            return left < right
        elif op == '<=':
            return left <= right

    def visitEqualityExpr(self, ctx: OperacionesComplParser.EqualityExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right

    def visitNotExpr(self, ctx: OperacionesComplParser.NotExprContext):
        operand = self.visit(ctx.expr())
        return not operand

    def visitAndExpr(self, ctx: OperacionesComplParser.AndExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left and right

    def visitOrExpr(self, ctx: OperacionesComplParser.OrExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left or right

    def visitNandExpr(self, ctx: OperacionesComplParser.NandExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return not (left and right)

    def visitXorExpr(self, ctx: OperacionesComplParser.XorExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left != right

# Función principal para leer la entrada y evaluar las expresiones
def calc(line) -> float:
    input_stream = InputStream(line)

    # Lexing
    lexer = OperacionesComplLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Parsing
    parser = OperacionesComplParser(stream)
    tree = parser.expr()

    # Utilizar el visitante personalizado para recorrer el AST
    visitor = ComplexVisitor()
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
