//Ejercicio 7
//Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : INT ID IGUAL NUM;

INT : 'int';
ID : [a-zA-Z]+;
IGUAL : '=';
NUM : [0-9]+;
WS : [ \t\r\n]+ -> skip;
