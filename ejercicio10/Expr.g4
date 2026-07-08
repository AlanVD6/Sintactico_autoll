//Ejercicio 10
//Numero de control 23030022

grammar Expr;
root : expr EOF;
expr : PRINT PARE_AB expr PARE_CI PUNTO_COMA|CADENA;

PRINT : 'print';
CADENA : '"' ~["\r\n]* '"';
PARE_AB : '(';
PARE_CI : ')';
PUNTO_COMA :';';
WS : [ \t\r\n]+ -> skip;