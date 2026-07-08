//ejercicio 1 - suma 
//Numero de control: 23030022

grammar Expr;

root : expr ;
expr : NUM MAS NUM;

NUM : [0-9]+;
MAS : '+';
WS : [ \t\r\n]+ -> skip;