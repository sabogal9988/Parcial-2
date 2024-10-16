import sys
from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser

# Clase para evaluar expresiones de MAP y FILTER
class MapFilterEvaluator:

    def visit(self, ctx):
        if ctx.MapFunction():
            function = ctx.function.getText()
            iterable = self.visit(ctx.iterable)
            return self.apply_map(function, iterable)
        elif ctx.FilterFunction():
            function = ctx.function.getText()
            iterable = self.visit(ctx.iterable)
            return self.apply_filter(function, iterable)

    def apply_map(self, function, iterable):
        # Simulación de la aplicación de la función sobre el iterable
        print(f"Aplicando MAP con función '{function}' a: {iterable}")
        return [self.simulate_function(function, x) for x in iterable]

    def apply_filter(self, function, iterable):
        # Simulación de la aplicación de la función condicional sobre el iterable
        print(f"Aplicando FILTER con función '{function}' a: {iterable}")
        return [x for x in iterable if self.simulate_condition(function, x)]

    def simulate_function(self, function, x):
        # Simulación de la función (puedes expandir esto según tus necesidades)
        if function == "square":
            return x ** 2
        return x

    def simulate_condition(self, function, x):
        # Simulación de una condición (puedes expandir esto según tus necesidades)
        if function == "even":
            return x % 2 == 0
        return True  # Por defecto, no filtra nada

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = MapLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapParser(stream)
    tree = parser.statement()

    evaluator = MapFilterEvaluator()
    result = evaluator.visit(tree)
    print("Resultado:", result)

if __name__ == '__main__':
    main()
