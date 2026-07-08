//Ejercicio 9 
//Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : IF PAREN_AB expr PAREN_CE |expr MAYOR expr | ID | NUM;

IF : 'if';
PAREN_AB: '(';
ID :  [a-zA-Z]+;
MAYOR : '>';
NUM : [0-9]+;
PAREN_CE: ')';
WS : [ \t\r\n]+ -> skip;