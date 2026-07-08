//ejercicio 3 
// Numero de control: 23030022

grammar Expr;

root : expr;
expr : ID IGUAL expr | ID | NUM;

ID: [a-zA-Z]+ ;
IGUAL : '=' ;
NUM : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;