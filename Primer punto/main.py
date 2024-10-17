import sys
from antlr4 import *
from OperacionesComplLexer import OperacionesComplLexer
from OperacionesComplParser import OperacionesComplParser
from OperacionesComplVisitor import OperacionesComplVisitor

class EvalVisitor(OperacionesComplVisitor):

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitNegExpr(self, ctx):
        return -self.visit(ctx.expr())

    def visitNotExpr(self, ctx):
        return not self.visit(ctx.expr())

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            return left / right if right != 0 else 'Error: Division by zero'

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitAtom(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.COMPLEX():
            return complex(ctx.COMPLEX().getText().replace('i', 'j'))
        elif ctx.BOOL():
            return True if ctx.getText() == 'true' else False

def main(argv):
    input_stream = FileStream(argv[1]) if len(argv) > 1 else InputStream(sys.stdin.read())

    lexer = OperacionesComplLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OperacionesComplParser(stream)
    tree = parser.expr()

    visitor = EvalVisitor()
    result = visitor.visit(tree)
    print("El Resultado es:", result)

if _name_ == '_main_':
    main(sys.argv)
