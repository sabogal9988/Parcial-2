# Parcial-2
Configuración del Entorno
Clonar el Repositorio

git clone https://github.com/sabogal9988/Parcial-2
cd Parcial-2
Crear un Entorno Virtual

python3 -m venv .venv
Activar el Entorno Virtual


activar en Linux:
source .venv/bin/activate
Instalar las Dependencias
sudo pip install antlr4-python3-runtime==4.13.2
sudo pip install numpy==2.1.2


# Primer Punto 
## archivos del punto 
- OperacioneCompl.g4
- test.py
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
python3 main.py
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
python3 main.py
```
# nota 
Puedes editar input2.txt para analizar diferentes expresiones complejas.
- MAP(square, [1, 2, 3, 4])
- FILTER(even, [10, 15, 20, 25])
- MAP(increment, (5, 6, 7))

# Punto tres 
## archivos del punto 
- Transformada.g4 : Gramática para el cálculo de la transformada de Fourier.
- test3.py: Script para analizar expresiones con la gramática generada.
# Generación del parser
1. Navega al directorio donde se encuentra Transformada.g4
2. ejecutar el siguiente comando
```bash
antlr4 -Dlanguage=Python3 FourierTransform.g4
```
Esto generará varios archivos .py, incluyendo TransformadaLexer.py y TransformadaParser.py.

# Ejecución del parser
Ejecuta el script de prueba con el siguiente comando:
```bash
python3 main.py
```
# nota 
Puedes editar input3.txt para analizar diferentes expresiones complejas.
-FOURIER([1, 2, 3, 4])
-FOURIER([0, 1, 0, -1, 0])
-FOURIER([10, 20, 30, 40])
