# Parcial-2
# Primer Punto 
## archivos del punto 
- OperacioneCompl.g4
- test.py
- input.txt
# Generación del parser
1. Navega al directorio donde se encuentra OperacionesCompl.g4
2. ejecutar el siguiente comando
```bash
antlr4 -Dlanguage=Python3 OperacionesCompl.g4
```
Esto generará varios archivos .py, incluyendo OperecionesComplLexer.py y OperecionesComplParser.py
# Ejecución del parser
Ejecuta el script de prueba con el siguiente comando:
```bash
python3 test.py < input.txt
```
# nota 
Puedes editar input.txt para analizar diferentes expresiones complejas.
- (2 + 7i) + (3 - 4i)
- (5 - 2i) * (3 + i)
- (10 + 4i) / (2 - 3i)

# Segundo Punto 
## archivos del punto 
- Map.g4 : Gramática para las funciones MAP
- test2.py: Script para analizar expresiones con la gramática generada.
- input2.txt :Archivo con ejemplos de uso de MAP
# Generación del parser
1. Navega al directorio donde se encuentra Map.g4
2. ejecutar el siguiente comando
```bash
antlr4 -Dlanguage=Python3 Map.g4
```
Esto generará varios archivos .py, incluyendo MapLexer.py y MapParser.py.

# Ejecución del parser
Ejecuta el script de prueba con el siguiente comando:
```bash
python3 test2.py < input2.txt
```
# nota 
Puedes editar input.txt para analizar diferentes expresiones complejas.
- MAP(square, [1, 2, 3, 4])
- FILTER(even, [10, 15, 20, 25])
- MAP(increment, (5, 6, 7))
