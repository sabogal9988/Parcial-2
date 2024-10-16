# Parcial-2
# Primer Punto 
## archivos del punto 
- OperacioneCompl.g4
- test.py
- input.py
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
