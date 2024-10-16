grammar OperacionesCompl;

expr: expr '+' expr      # Addition
    | expr '-' expr      # Subtraction
    | expr '*' expr      # Multiplication
    | expr '/' expr      # Division
    | '(' expr ')'       # ParenthesizedExpression
    | COMPLEX            # ComplexNumber
    | REAL               # RealNumber
    ;

COMPLEX: REAL ('+'|'-') REAL 'i';
REAL: [0-9]+ ('.' [0-9]+)?;

WS: [ \t\r\n]+ -> skip;
