from antlr4 import *
from CalculatorLexer import CalculatorLexer


class CalculatorVisitor(ParseTreeVisitor):
    # | INT                     # int
    def visitInt(self, ctx):
        return int(ctx.getText())

    # | expr op=('+'|'-') expr  # AddSub
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == CalculatorLexer.ADD:
            return left + right
        else:
            return left - right

    # | expr op=('*'|'/') expr  # MULDiv
    def visitMULDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == CalculatorLexer.MUL:
            return left * right
        else:
            return left / right

    # | op=('-'|'+') INT       # prehead1
    def visitPrehead1(self, ctx):
        value = int(ctx.INT().getText())
        if ctx.op.type == CalculatorLexer.ADD:
            return value
        else:
            return -(value)

    # | op=('-'|'+') '(' expr ')'      # prehead2
    def visitPrehead2(self, ctx):
        value = self.visit(ctx.expr())
        if ctx.op.type == CalculatorLexer.ADD:
            return self.visit(ctx.expr())
        else:
            return -self.visit(ctx.expr())

    # | '(' expr ')'            # parens
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
