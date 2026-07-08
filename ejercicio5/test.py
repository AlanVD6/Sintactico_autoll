#Ejercicio 5
#Numero de control: 23030022

from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

entrada = input("Código: ")
stream = InputStream(entrada)
lexer = ExprLexer(stream)              
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
arbol = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
    print("Código correcto")
    print("Árbol: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El código tiene errores de sintaxis")
    