//Ejercicio 8
//Numero de control 23030022

grammar Expr;

root : expr EOF;
expr : ID MAYOR_QUE expr | ID | NUM;

ID : [a-zA-Z]+;
MAYOR_QUE : '>=';
NUM : [0-9]+;
WS : [ \t\r\n]+ -> skip;