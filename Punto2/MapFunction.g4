grammar MapFunction;
prog:   stat+ ;

stat:   mapFunction NEWLINE
    |   filterFunction NEWLINE
    ;
mapFunction: 'map' '(' lambdaExpr ',' iterable ')' ;
filterFunction: 'filter' '(' lambdaExpr ',' iterable ')' ;
iterable:list|tuple;
list: '[' elements? ']' ;
tuple: '(' elements? ')' ;
function: ID op var|ID'.upper()'|ID'.lower()'|ID'.capitalize()'|'len('ID')'(op var)?|ID op var op var (' and '|' or ')? function?|ID'['INT']' (op var)?;
elements: expr (',' expr)* ;
lambdaExpr: 'lambda' ID ':' function;
op: '+'|'-'|'*'|'/'|'%'|'**'|'.'ID'()'|'=='|'!='|'<'|'>'|'<='|'>=';
var: ID|INT|FLOAT;
expr: INT | FLOAT | STRING ;
INT: [0-9]+;
ID: [a-zA-Z]+;
FLOAT: [0-9]+'.'[0-9]+;
STRING: '"' .*? '"';
MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace

