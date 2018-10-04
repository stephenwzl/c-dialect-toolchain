import sys
from antlr4 import *
from grammar.ObjectiveCLexer import ObjectiveCLexer
from grammar.ObjectiveCParser import ObjectiveCParser
from grammar.ObjectiveCParserListener import ObjectiveCParserListener
from codegen.symbol_table import SymbolTable

def main(argv):
    fileInput = FileStream(argv[1], encoding='utf-8')
    lexer = ObjectiveCLexer(input=fileInput)
    stream = CommonTokenStream(lexer)
    preprocessor_parser = ObjectiveCParser(stream)
    listener = ObjectiveCParserListener()
    walker = ParseTreeWalker()
    walker.walk(listener, preprocessor_parser.translationUnit())
    print SymbolTable.shared_instance().table


if __name__ == '__main__':
    main(sys.argv)
