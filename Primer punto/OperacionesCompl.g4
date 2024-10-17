grammar OperacionesCompl;

expr:  '(' expr ')'                # ParenExpr
    |   '-' expr                   # NegExpr
    |   '!' expr                   # NotExpr
    |   atom                       # AtomExpr
    |   expr op=('*'|'/') expr     # MulDivExpr
    |   expr op=('+'|'-') expr     # AddSubExpr
    |   expr op=('>'|'>='|'<'|'<=') expr  # CompExpr
    |   expr op=('=='|'!=') expr   # EqualityExpr
    |   expr '&&' expr             # AndExpr
    |   expr '||' expr             # OrExpr
    |   expr '~' expr              # NandExpr
    |   expr '?' expr              # XorExpr
    ;

atom: COMPLEX
    | INT
    | BOOL
    ;

COMPLEX: REAL_PART ( ('+'|'-')? IMAGINARY_PART )?
       | IMAGINARY_PART
       ;

// tokens expresados como expresiones regulares
INT : [0-9]+ ;
IMAGINARY_PART: [0-9]* 'i' ;
REAL_PART: [0-9]+ ('.' [0-9]+)? ;
BOOL: 'true' | 'false' ;

WS  : [ \t\n\r]+ -> skip ;
