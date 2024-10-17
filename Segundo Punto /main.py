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
        # Evalúa el contenido de la tupla
        return [evaluate(e) for e in ctx.elemento()]

    elif isinstance(ctx, MapParser.ListaContext):
        # Evalúa el contenido de la lista
        return [evaluate(e) for e in ctx.elemento()]

    elif isinstance(ctx, MapParser.MapContext):
        # Simula el comportamiento de una función MAP en una lista o tupla
        function = ctx.functionm().getText()  # Obtener el texto de la función
        iterable = evaluate(ctx.iterable())  # Evaluar el iterable
        print(f"Aplicando MAP con función '{function}' a: {iterable}")
        return [simulate_function(function, x) for x in iterable]

def simulate_function(function, x):
    # Simulación de la función (puedes expandir esto según tus necesidades)
    if function == "square":
        return x ** 2
    elif function == "cube":
        return x ** 3
    elif function == "increment":
        return x + 1
    elif function == "decrement":
        return x - 1
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
