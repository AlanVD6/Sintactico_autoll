#Ejercicio 2 
#Numero de control: 23030022

from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

entrada = input("Código: ")
lexer = ExprLexer(entrada)
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
arbol = parser.root()

#print ("Árbol: ")
#print (arbol.toStringTree(recog=parser))

if parser.getNumberOfSyntaxErrors() == 0:
    print("Código correcto")
    print("Árbol: ")
    print (arbol.toStringTree(recog=parser))
else :
    print("El código tiene errores de sintaxis")
    