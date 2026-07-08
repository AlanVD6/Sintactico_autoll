//ejercicio 2 - resta
//Numero de control: 23030022

grammar Expr;

root : expr ;
expr : expr MENOS expr | NUM;

NUM : [0-9]+;
MAS : '+';
MENOS : '-';
WS : [ \t\r\n]+ -> skip;