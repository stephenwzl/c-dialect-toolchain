import sys
from antlr4 import *
from grammar.ObjectiveCLexer import ObjectiveCLexer
from grammar.ObjectiveCParser import ObjectiveCParser
from grammar.ObjectiveCPreprocessorParser import ObjectiveCPreprocessorParser
from grammar.ObjectiveCParserVisitor import ObjectiveCParserVisitor
from grammar.ObjectiveCPreprocessorParserVisitor import ObjectiveCPreprocessorParserVisitor


def main(argv):
    fileInput = FileStream(argv[1], encoding='utf-8')
    lexer = ObjectiveCLexer(input=fileInput)
    stream = CommonTokenStream(lexer)
    preprocessor_parser = ObjectiveCParser(stream)
    visitor = ObjectiveCParserVisitor()
    visitor.visit(preprocessor_parser.translationUnit())


if __name__ == '__main__':
    main(sys.argv)
