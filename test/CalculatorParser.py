# Generated from Calculator.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\n\37\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\5\2\22\n\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\32")
        buf.write(u"\n\2\f\2\16\2\35\13\2\3\2\2\3\2\3\2\2\4\3\2\b\t\3\2\6")
        buf.write(u"\7\2\"\2\21\3\2\2\2\4\5\b\2\1\2\5\22\7\5\2\2\6\7\7\3")
        buf.write(u"\2\2\7\b\5\2\2\2\b\t\7\4\2\2\t\22\3\2\2\2\n\13\t\2\2")
        buf.write(u"\2\13\22\7\5\2\2\f\r\t\2\2\2\r\16\7\3\2\2\16\17\5\2\2")
        buf.write(u"\2\17\20\7\4\2\2\20\22\3\2\2\2\21\4\3\2\2\2\21\6\3\2")
        buf.write(u"\2\2\21\n\3\2\2\2\21\f\3\2\2\2\22\33\3\2\2\2\23\24\f")
        buf.write(u"\b\2\2\24\25\t\3\2\2\25\32\5\2\2\t\26\27\f\7\2\2\27\30")
        buf.write(u"\t\2\2\2\30\32\5\2\2\b\31\23\3\2\2\2\31\26\3\2\2\2\32")
        buf.write(u"\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\3\3\2\2\2")
        buf.write(u"\35\33\3\2\2\2\5\21\31\33")
        return buf.getvalue()


class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"<INVALID>", u"'*'", 
                     u"'/'", u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"INT", 
                      u"MUL", u"DIV", u"ADD", u"SUB", u"WS" ]

    RULE_expr = 0

    ruleNames =  [ u"expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INT=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    WS=8

    def __init__(self, input, output=sys.stdout):
        super(CalculatorParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalculatorParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(CalculatorParser.ExprContext, self).copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalculatorParser.ExprContext)
            super(CalculatorParser.ParensContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParens"):
                listener.enterParens(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParens"):
                listener.exitParens(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitParens"):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class Prehead1Context(ExprContext):

        def __init__(self, parser, ctx): # actually a CalculatorParser.ExprContext)
            super(CalculatorParser.Prehead1Context, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalculatorParser.INT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPrehead1"):
                listener.enterPrehead1(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPrehead1"):
                listener.exitPrehead1(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPrehead1"):
                return visitor.visitPrehead1(self)
            else:
                return visitor.visitChildren(self)


    class Prehead2Context(ExprContext):

        def __init__(self, parser, ctx): # actually a CalculatorParser.ExprContext)
            super(CalculatorParser.Prehead2Context, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPrehead2"):
                listener.enterPrehead2(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPrehead2"):
                listener.exitPrehead2(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPrehead2"):
                return visitor.visitPrehead2(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalculatorParser.ExprContext)
            super(CalculatorParser.AddSubContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterAddSub"):
                listener.enterAddSub(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAddSub"):
                listener.exitAddSub(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAddSub"):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class MULDivContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalculatorParser.ExprContext)
            super(CalculatorParser.MULDivContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterMULDiv"):
                listener.enterMULDiv(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMULDiv"):
                listener.exitMULDiv(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMULDiv"):
                return visitor.visitMULDiv(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalculatorParser.ExprContext)
            super(CalculatorParser.IntContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalculatorParser.INT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterInt"):
                listener.enterInt(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInt"):
                listener.exitInt(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitInt"):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = CalculatorParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(CalculatorParser.INT)
                pass

            elif la_ == 2:
                localctx = CalculatorParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 4
                self.match(CalculatorParser.T__0)
                self.state = 5
                self.expr(0)
                self.state = 6
                self.match(CalculatorParser.T__1)
                pass

            elif la_ == 3:
                localctx = CalculatorParser.Prehead1Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==CalculatorParser.ADD or _la==CalculatorParser.SUB):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 9
                self.match(CalculatorParser.INT)
                pass

            elif la_ == 4:
                localctx = CalculatorParser.Prehead2Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==CalculatorParser.ADD or _la==CalculatorParser.SUB):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 11
                self.match(CalculatorParser.T__0)
                self.state = 12
                self.expr(0)
                self.state = 13
                self.match(CalculatorParser.T__1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 23
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorParser.MULDivContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 18
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculatorParser.MUL or _la==CalculatorParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 19
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = CalculatorParser.AddSubContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 21
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculatorParser.ADD or _la==CalculatorParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        self.expr(6)
                        pass

             
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




