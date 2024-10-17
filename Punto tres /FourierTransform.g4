grammar FourierTransform;

// Reglas principales para transformadas de Fourier
statement: 'FOURIER' '(' exprList ')' # FourierTransform
         | 'FOURIER_INV' '(' exprList ')' # InverseFourierTransform
         ;

// Lista de expresiones que acepta múltiples expresiones separadas por comas
exprList: expr (',' expr)*;

// Expresiones que pueden ser números reales, identificadores o algunas funciones comunes
expr: REAL
    | IDENTIFIER
    | 'rect' '(' 't' '/' 'T' ')' # Rectangular function
    | 'tri' '(' 't' '/' 'T' ')' # Triangular function
    | 'cos' '(' 'w0' ',' 't' ')' # Cosine function
    | 'sin' '(' 'w0' ',' 't' ')' # Sine function
    | 'delta' '(' 't' ')' # Delta function
    ;

// Definición de identificadores y números reales
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
REAL: [0-9]+ ('.' [0-9]+)?;

// Ignorar espacios en blanco y tabulaciones
WS: [ \t\r\n]+ -> skip;
