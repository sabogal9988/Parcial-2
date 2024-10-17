import sys
from antlr4 import *
from OperacionesComplLexer import OperacionesComplLexer
from OperacionesComplParser import OperacionesComplParser
import cmath

# Función recursiva para evaluar el árbol de sintaxis.
def evaluate(ctx):
    if isinstance(ctx, OperacionesComplParser.AddSubExprContext):
        left = evaluate(ctx.expr(0))
        right = evaluate(ctx.expr(1))
        op = ctx.op.text
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    elif isinstance(ctx, OperacionesComplParser.MulDivExprContext):
        left = evaluate(ctx.expr(0))
        right = evaluate(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                print("¡División por cero!")
                return 0
            return left / right

    elif isinstance(ctx, OperacionesComplParser.AtomExprContext):
        if 'i' in ctx.getText():  # Check if the atom is imaginary
            return complex(ctx.getText().replace('i', 'j'))  # Replace 'i' with 'j' for Python's complex numbers
        else:
            return complex(float(ctx.getText()), 0)

    elif isinstance(ctx, OperacionesComplParser.ParenExprContext):
        return evaluate(ctx.expr())

    elif isinstance(ctx, OperacionesComplParser.ComparisonExprContext):
        left = evaluate(ctx.expr(0))
        right = evaluate(ctx.expr(1))
        op = ctx.op.text
        if op == '>':
            return left > right
        elif op == '>=':
            return left >= right
        elif op == '<':
            return left < right
        elif op == '<=':
            return left <= right

    elif isinstance(ctx, OperacionesComplParser.EqualityExprContext):
        left = evaluate(ctx.expr(0))
        right = evaluate(ctx.expr(1))
        op = ctx.op.text
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right

    elif isinstance(ctx, OperacionesComplParser.NotExprContext):
        operand = evaluate(ctx.expr())
        return not operand

    elif isinstance(ctx, OperacionesComplParser.AndExprContext):
        left = evaluate(ctx.expr(0))
        right = evaluate(ctx.expr(1))
        return left and right

    elif isinstance(ctx, OperacionesComplParser.OrExprContext):
        left = evaluate(ctx.expr(0))
        right = evaluate(ctx.expr(1))
        return left or right

    elif isinstance(ctx, OperacionesComplParser.NandExprContext):
        left = evaluate(ctx.expr(0))
        right = evaluate(ctx.expr(1))
        return not (left and right)

    elif isinstance(ctx, OperacionesComplParser.XorExprContext):
        left = evaluate(ctx.expr(0))
        right = evaluate(ctx.expr(1))
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
