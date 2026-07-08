//Ejercicio 6
// Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : expr MULTIPLICACION expr | expr SUMA expr| NUM;

NUM : [0-9]+;
MULTIPLICACION : '*';
SUMA : '+';
WS : [ \t\r\n]+ -> skip;