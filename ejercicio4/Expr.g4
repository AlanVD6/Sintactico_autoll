//ejercicio 4
// Numero de control: 23030022

grammar Expr;

root : expr;
expr : IF expr | expr MAYOR_QUE expr | ID | NUM;

IF : 'if';
ID: [a-zA-Z]+ ;
MAYOR_QUE: '>';
NUM : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
