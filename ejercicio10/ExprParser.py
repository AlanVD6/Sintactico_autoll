# Generated from ./Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,17,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,15,8,1,1,1,0,0,2,0,2,0,0,15,0,4,1,0,0,0,2,14,1,0,0,0,4,5,3,2,
        1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,5,1,0,0,8,9,5,3,0,0,9,10,3,2,1,0,
        10,11,5,4,0,0,11,12,5,5,0,0,12,15,1,0,0,0,13,15,5,2,0,0,14,7,1,0,
        0,0,14,13,1,0,0,0,15,3,1,0,0,0,1,14
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "<INVALID>", "'('", "')'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "CADENA", "PARE_AB", "PARE_CI", 
                      "PUNTO_COMA", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    PRINT=1
    CADENA=2
    PARE_AB=3
    PARE_CI=4
    PUNTO_COMA=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def PARE_AB(self):
            return self.getToken(ExprParser.PARE_AB, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PARE_CI(self):
            return self.getToken(ExprParser.PARE_CI, 0)

        def PUNTO_COMA(self):
            return self.getToken(ExprParser.PUNTO_COMA, 0)

        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(ExprParser.PRINT)
                self.state = 8
                self.match(ExprParser.PARE_AB)
                self.state = 9
                self.expr()
                self.state = 10
                self.match(ExprParser.PARE_CI)
                self.state = 11
                self.match(ExprParser.PUNTO_COMA)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(ExprParser.CADENA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





