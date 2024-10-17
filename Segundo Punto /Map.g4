grammar Map;

// Reglas principales para funciones MAP y FILTER
statement: map | filter;

// Definición de la regla para MAP
map: MAP '(' functionm ',' iterable ')' ;

// Definición de la regla para FILTER
filter: FILTER '(' functionf ',' iterable ')' ;

// Funciones MAP disponibles
functionm: 'square'
         | 'cube'
         | 'increment'
         | 'decrement'
         ;

// Funciones FILTER disponibles
functionf: 'even'
         | 'odd'
         | 'positive'
         | 'negative'
         ;

// Iterables que pueden ser tuplas o listas
iterable: tupla | lista ;

// Definición de tuplas y listas
tupla: '(' elemento (',' elemento)* ')' ;
lista: '[' elemento (',' elemento)* ']' ;

// Un elemento es un número
elemento: NUMERO ;

// Definición de números
NUMERO: ('0' | [1-9] [0-9]*) ;

// Palabras reservadas
MAP: 'MAP' ;
FILTER: 'FILTER' ;

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip ;
