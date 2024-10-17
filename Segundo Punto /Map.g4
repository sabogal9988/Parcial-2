grammar Map;

funcion:    map
            |filter
            ;

map: MAP '(' functionm ',' iterable ')';
filter: FILTER '(' functionf ',' iterable ')';

//funciones MAP
functionm:  suma                    
            |resta
            |mult
            |div
            ;

//funciones FILTER
functionf:  mayor
            |menor
            |igual
            ;

iterable:   tupla
            |lista
            ;

suma: elemento '+';
resta: elemento '-';
mult: elemento '*' ;
div: elemento '/';

mayor: elemento '>';
menor: elemento'<';
igual: elemento '==';
mayor_igual: elemento '>=';
menor_igual: elemento '<=';

tupla: '(' elemento (',' elemento)* ')';
lista: '[' elemento (',' elemento)* ']';

elemento: NUMERO ;

NUMERO: ('0' | [1-9] [0-9]*) ;

MAP: 'map';
FILTER: 'filter';

WS: [ \t\r]+ -> skip;
