grammar Map;

statement: 'MAP' '(' function ',' iterable ')'    # MapFunction
         | 'FILTER' '(' function ',' iterable ')' # FilterFunction
         ;

function: IDENTIFIER;
iterable: '[' exprList ']' | '(' exprList ')' | IDENTIFIER;
exprList: expr (',' expr)*;
expr: REAL | IDENTIFIER;

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
REAL: [0-9]+ ('.' [0-9]+)?;

WS: [ \t\r\n]+ -> skip;
