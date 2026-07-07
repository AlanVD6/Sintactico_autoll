//ejercicio 3 
// Numero de control: 23030022

grammar Expr;

root : expr;
expr : expr ID IGUAL expr | expr NUM expr;

ID: [a-zA-Z]+ ;
IGUAL : '=' ;
NUM : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;