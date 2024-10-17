import sys
from antlr4 import *
from MapLexer import MapLexer
from MapParser import MapParser
from MapVisitor import MapVisitor  # Asumiendo que hay una clase base de visitante generada

# Clase para evaluar expresiones de listas, tuplas y map
class FuncVisitor(MapVisitor):
    # Visit a parse tree produced by MapParser#elemento.
    def visitElemento(self, ctx:MapParser.ElementoContext):
        # Asumiendo que un 'elemento' es un número
        return int(ctx.getText())
    
    # Visit a parse tree produced by MapParser#tupla.
    def visitTupla(self, ctx:MapParser.TuplaContext):
        # Evalúa el contenido de la tupla, transformándolo en un objeto Python
        return eval(ctx.getText())

    # Visit a parse tree produced by MapParser#lista.
    def visitLista(self, ctx:MapParser.ListaContext):
        # Evalúa el contenido de la lista, transformándolo en un objeto Python
        return eval(ctx.getText())

    # Visit a parse tree produced by MapParser#map.
    def visitMap(self, ctx:MapParser.MapContext):
        # Simula el comportamiento de una función MAP en una lista
        function = ctx.function().getText()  # Obtener el texto de la función
        iterable = self.visit(ctx.iterable())  # Visitar el iterable para obtener la lista
        print(f"Aplicando MAP con función '{function}' a: {iterable}")
        return [self.simulate_function(function, x) for x in iterable]

    def simulate_function(self, function, x):
        # Simulación de la función (puedes expandir esto según tus necesidades)
        if function == "square":
            return x ** 2
        return x

def calc(line) -> float:
    input_stream = InputStream(line)

    # Lexing
    lexer = MapLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Parsing
    parser = MapParser(stream)
    tree = parser.statement()  # Asumiendo que el punto de entrada de la gramática es 'statement'

    # Utilizar el visitante personalizado para recorrer el AST
    visitor = FuncVisitor()
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
