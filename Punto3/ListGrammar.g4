grammar ListGrammar;
prog:stat+ ;
stat: list NEWLINE;
list: '[' element (',' element)* ']';
element : NUMBER;
NUMBER: '-'?('0'..'9')+ ('.' ('0'..'9')+)? ('e' ('+'|'-') ('0'..'9')+)?;
NEWLINE:'\r'? '\n' ;
WS : [ \t\r\n]+ -> skip;
