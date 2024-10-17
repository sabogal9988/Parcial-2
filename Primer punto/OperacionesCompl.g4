grammar OperacionesCompl;

expr: expr '+' expr      # Addition
    | expr '-' expr      # Subtraction
    | expr '*' expr      # Multiplication
    | expr '/' expr      # Division
    | '(' expr ')'       # ParenthesizedExpression
    | COMPLEX            # ComplexNumber
    | REAL               # RealNumber
expr:  '(' expr ')'             # ParenExpr
    |   '!' expr                 # NotExpr
    |   atom                     # AtomExpr
    |   expr op=('*'|'/') expr   # MulDivExpr
    |   expr op=('+'|'-') expr   # AddSubExpr
    |   expr op=('>'|'>='|'<'|'<=') expr  # ComparisonExpr
    |   expr op=('=='|'!=') expr  # EqualityExpr
    |   expr '&&' expr            # AndExpr
    |   expr '||' expr            # OrExpr
    |   expr '~' expr             # NandExpr
    |   expr '?' expr             # XorExpr
;

COMPLEX: REAL ('+'|'-') REAL 'i';
REAL: [0-9]+ ('.' [0-9]+)?;
atom: INT
    | IMAGINARY
    | 'true'
    | 'false'
    ;

WS: [ \t\r\n]+ -> skip;
// tokens expressed as regular expressions
INT : [0-9]+ ;
IMAGINARY: REAL_PART 'i' ;
REAL_PART: [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t]+ -> skip ;
