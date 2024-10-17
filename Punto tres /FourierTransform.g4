grammar FourierTransform;

// Reglas principales para transformadas de Fourier
statement: 'FOURIER' '(' exprList ')' # FourierTransform
         | 'FOURIER_INV' '(' exprList ')' # InverseFourierTransform
         ;

// Lista de expresiones que acepta múltiples expresiones separadas por comas
exprList: expr (',' expr)* ;

// Expresiones que pueden ser números reales, identificadores o algunas funciones comunes
expr: REAL
    | IDENTIFIER
    | rect 
    | tri
    | cos
    | sin
    | delta
    ;

// Definición de las funciones específicas
rect: 'rect' '(' 't' '/' 'T' ')'; // Función rectangular
tri: 'tri' '(' 't' '/' 'T' ')'; // Función triangular
cos: 'cos' '(' 'w0' ',' 't' ')'; // Función coseno
sin: 'sin' '(' 'w0' ',' 't' ')'; // Función seno
delta: 'delta' '(' 't' ')'; // Función delta

// Definición de identificadores y números reales
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]* ;
REAL: [0-9]+ ('.' [0-9]+)? ;

// Ignorar espacios en blanco y tabulaciones
WS: [ \t\r\n]+ -> skip ;
