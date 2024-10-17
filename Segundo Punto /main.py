import sys
from antlr4 import *
from MapLexer import MapLexer
from MapParser import MapParser
from MapVisitor import MapVisitor

# Clase para evaluar expresiones de listas, tuplas y map
class FuncVisitor(MapVisitor):
    def visitElemento(self, ctx: MapParser.ElementoContext):
        return int(ctx.getText())
    
    def visitTupla(self, ctx: MapParser.TuplaContext):
        return [self.visit(e) for e in ctx.elemento()]

    def visitLista(self, ctx: MapParser.ListaContext):
        return [self.visit(e) for e in ctx.elemento()]

    def visitMap(self, ctx: MapParser.MapContext):
        function = ctx.functionm().getText()  # Obtener el texto de functionm
        iterable = self.visit(ctx.iterable())
        print(f"Aplicando MAP con función '{function}' a: {iterable}")
        return [self.simulate_function(function, x) for x in iterable]

    def simulate_function(self, function, x):
        if function == "square":
            return x ** 2
        elif function == "cube":
            return x ** 3
        elif function == "increment":
            return x + 1
        elif function == "decrement":
            return x - 1
        return x

def calc(line) -> float:
    input_stream = InputStream(line)
    lexer = MapLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapParser(stream)
    tree = parser.statement()
    visitor = FuncVisitor()
    return visitor.visit(tree)

if _name_ == '_main_':
    while True:
        print(">>> ", end='')
        line = input()
        if line.lower() == 'exit':
            break
        try:
            print(calc(line))
        except Exception as e:
            print("Error:", e)
