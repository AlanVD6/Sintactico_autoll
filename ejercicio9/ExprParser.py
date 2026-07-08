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
        4,1,7,26,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,16,8,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,1,0,1,2,
        2,0,2,0,0,26,0,4,1,0,0,0,2,15,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,
        1,1,0,0,0,7,8,6,1,-1,0,8,9,5,1,0,0,9,10,5,2,0,0,10,11,3,2,1,0,11,
        12,5,6,0,0,12,16,1,0,0,0,13,16,5,3,0,0,14,16,5,5,0,0,15,7,1,0,0,
        0,15,13,1,0,0,0,15,14,1,0,0,0,16,22,1,0,0,0,17,18,10,3,0,0,18,19,
        5,4,0,0,19,21,3,2,1,4,20,17,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,
        22,23,1,0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,2,15,22
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "<INVALID>", "'>'", "<INVALID>", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "IF", "PAREN_AB", "ID", "MAYOR", "NUM", 
                      "PAREN_CE", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    IF=1
    PAREN_AB=2
    ID=3
    MAYOR=4
    NUM=5
    PAREN_CE=6
    WS=7

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
            self.expr(0)
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

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def PAREN_AB(self):
            return self.getToken(ExprParser.PAREN_AB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def PAREN_CE(self):
            return self.getToken(ExprParser.PAREN_CE, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def MAYOR(self):
            return self.getToken(ExprParser.MAYOR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 8
                self.match(ExprParser.IF)
                self.state = 9
                self.match(ExprParser.PAREN_AB)
                self.state = 10
                self.expr(0)
                self.state = 11
                self.match(ExprParser.PAREN_CE)
                pass
            elif token in [3]:
                self.state = 13
                self.match(ExprParser.ID)
                pass
            elif token in [5]:
                self.state = 14
                self.match(ExprParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 17
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 18
                    self.match(ExprParser.MAYOR)
                    self.state = 19
                    self.expr(4) 
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




