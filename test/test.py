import sys

from antlr4 import *
from CalculatorParser import CalculatorParser
from CalculatorLexer import CalculatorLexer
from CalculatorListener import CalculatorListener
from CalculatorVisitor import CalculatorVisitor


def main(argv):
    input = FileStream(argv[1])
    lexer = CalculatorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CalculatorParser(stream)
    tree = parser.expr()
    v = CalculatorVisitor()
    print v.visit(tree)


if __name__ == '__main__':
    main(sys.argv)