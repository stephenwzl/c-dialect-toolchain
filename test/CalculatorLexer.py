# Generated from Calculator.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\n+\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\4\6\4\31\n\4\r\4")
        buf.write(u"\16\4\32\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t&\n\t")
        buf.write(u"\r\t\16\t\'\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write(u"\t\21\n\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2,\2\3\3\2\2")
        buf.write(u"\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write(u"\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\25")
        buf.write(u"\3\2\2\2\7\30\3\2\2\2\t\34\3\2\2\2\13\36\3\2\2\2\r \3")
        buf.write(u"\2\2\2\17\"\3\2\2\2\21%\3\2\2\2\23\24\7*\2\2\24\4\3\2")
        buf.write(u"\2\2\25\26\7+\2\2\26\6\3\2\2\2\27\31\t\2\2\2\30\27\3")
        buf.write(u"\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\b")
        buf.write(u"\3\2\2\2\34\35\7,\2\2\35\n\3\2\2\2\36\37\7\61\2\2\37")
        buf.write(u"\f\3\2\2\2 !\7-\2\2!\16\3\2\2\2\"#\7/\2\2#\20\3\2\2\2")
        buf.write(u"$&\t\3\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2")
        buf.write(u"()\3\2\2\2)*\b\t\2\2*\22\3\2\2\2\5\2\32\'\3\b\2\2")
        return buf.getvalue()


class CalculatorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INT = 3
    MUL = 4
    DIV = 5
    ADD = 6
    SUB = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'('", u"')'", u"'*'", u"'/'", u"'+'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"INT", u"MUL", u"DIV", u"ADD", u"SUB", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"INT", u"MUL", u"DIV", u"ADD", u"SUB", 
                  u"WS" ]

    grammarFileName = u"Calculator.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(CalculatorLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


