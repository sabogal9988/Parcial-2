import sys
from antlr4 import *
from MapLexer import MapLexer
from MapParser import MapParser

# Función recursiva para evaluar el árbol de sintaxis
def evaluate(ctx):
    if isinstance(ctx, MapParser.ElementoContext):
        # Asumiendo que un 'elemento' es un número
        return int(ctx.getText())

    elif isinstance(ctx, MapParser.TuplaContext):
        # Evalúa el contenido de la tupla, transformándolo en un objeto Python
        return eval(ctx.getText())

    elif isinstance(ctx, MapParser.ListaContext):
        # Evalúa el contenido de la lista, transformándolo en un objeto Python
        return eval(ctx.getText())

    elif isinstance(ctx, MapParser.MapContext):
        # Simula el comportamiento de una función MAP en una lista
        function = ctx.function().getText()  # Obtener el texto de la función
        iterable = evaluate(ctx.iterable())  # Evaluar el iterable para obtener la lista
        print(f"Aplicando MAP con función '{function}' a: {iterable}")
        return [simulate_function(function, x) for x in iterable]

def simulate_function(function, x):
    # Simulación de la función (puedes expandir esto según tus necesidades)
    if function == "square":
        return x ** 2
    return x

# Función principal para leer la entrada y evaluar las expresiones
def calc(line) -> float:
    input_stream = InputStream(line)

    # Lexing
    lexer = MapLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Parsing
    parser = MapParser(stream)
    tree = parser.statement()  # Asumiendo que el punto de entrada de la gramática es 'statement'

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
