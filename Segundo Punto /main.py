from antlr4 import *
from MapLexer import MapLexer
from MapParser import MapParser
from MapVisitor import MapVisitor  # Asumiendo que hay una clase base de visitante generada

# Clase para evaluar expresiones de listas, tuplas y map
class FuncVisitor(MapVisitor):
    # Visit a parse tree produced by MapParser#elemento.
    def visitElemento(self, ctx:MapParser.ElementoContext):
# Función recursiva para evaluar el árbol de sintaxis
def evaluate(ctx):
    if isinstance(ctx, MapParser.ElementoContext):
# Asumiendo que un 'elemento' es un número
return int(ctx.getText())
    
    # Visit a parse tree produced by MapParser#tupla.
    def visitTupla(self, ctx:MapParser.TuplaContext):

    elif isinstance(ctx, MapParser.TuplaContext):
# Evalúa el contenido de la tupla, transformándolo en un objeto Python
return eval(ctx.getText())

    # Visit a parse tree produced by MapParser#lista.
    def visitLista(self, ctx:MapParser.ListaContext):
    elif isinstance(ctx, MapParser.ListaContext):
# Evalúa el contenido de la lista, transformándolo en un objeto Python
return eval(ctx.getText())

    # Visit a parse tree produced by MapParser#map.
    def visitMap(self, ctx:MapParser.MapContext):
    elif isinstance(ctx, MapParser.MapContext):
# Simula el comportamiento de una función MAP en una lista
function = ctx.function().getText()  # Obtener el texto de la función
        iterable = self.visit(ctx.iterable())  # Visitar el iterable para obtener la lista
        iterable = evaluate(ctx.iterable())  # Evaluar el iterable para obtener la lista
print(f"Aplicando MAP con función '{function}' a: {iterable}")
        return [self.simulate_function(function, x) for x in iterable]
        return [simulate_function(function, x) for x in iterable]

    def simulate_function(self, function, x):
        # Simulación de la función (puedes expandir esto según tus necesidades)
        if function == "square":
            return x ** 2
        return x
def simulate_function(function, x):
    # Simulación de la función (puedes expandir esto según tus necesidades)
    if function == "square":
        return x ** 2
    return x

# Función principal para leer la entrada y evaluar las expresiones
def calc(line) -> float:
input_stream = InputStream(line)

@@ -46,9 +42,8 @@ def calc(line) -> float:
parser = MapParser(stream)
tree = parser.statement()  # Asumiendo que el punto de entrada de la gramática es 'statement'

    # Utilizar el visitante personalizado para recorrer el AST
    visitor = FuncVisitor()
    return visitor.visit(tree)
    # Evaluar el árbol de forma recursiva
    return evaluate(tree)

if __name__ == '__main__':
while True:
