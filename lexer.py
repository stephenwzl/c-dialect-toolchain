
import ply.lex as lex

tokens = (
    'AUTO', 'BREAK', 'CASE', 'CHAR', 'CONST',
    'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE', 'ELSE',
    'ENUM', 'EXTERN', 'FLOAT', 'FOR', 'GOTO',
    'IF', 'INT', 'LONG', 'REGISTER', 'RETURN',
    'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT',
    'SWITCH', 'TYPEDEF', 'UNION', 'UNSIGNED', 'VOID',
    'VOLATILE', 'WHILE', 'DELSPEC', 'DLLIMPORT', 'DLLEXPORT',
    'ELLIPSIS', 'RIGHT_ASSIGN', 'LEFT_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN',
    'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'XOR_ASSIGN',
    'OR_ASSIGN', 'RIGHT_OP', 'LEFT_OP', 'INC_OP', 'DEC_OP',
    'PTR_OP', 'AND_OP', 'OR_OP', 'LE_OP', 'GE_OP',
    'EQ_OP', 'NE_OP', 'SUPER',
    'SEMI', 'LBRACE', 'RBRACE', 'COMMA', 'LBRACK', 'RBRACK',
    'LP', 'RP', 'COLON', 'ASSIGN', 'DOT', 'AND',
    'EXMARK', 'WAVE', 'SUB', 'ADD', 'MUL', 'DIV', 'MOD', 'XOR',
    'GE', 'LE', 'OR', 'QUESTION',
    'IDENTIFIER', 'HEX_CONSTANT', 'OCT_CONSTANT', 'DEC_CONSTANT',
    'SCIENCE_COUNT', 'DECIMAL', 'C_STRING', 'OBJC_STRING',
    'INTERFACE', 'END'
)

t_AUTO = r'auto'
t_BREAK = r'break'
t_CASE = r'case'
t_CHAR = r'char'
t_CONST = r'const'

t_CONTINUE = r'continue'
t_DEFAULT = r'default'
t_DO = r'do'
t_DOUBLE = r'double'
t_ELSE = r'else'

t_ENUM = r'enum'
t_EXTERN = r'extern'
t_FLOAT = r'float'
t_FOR = r'for'
t_GOTO = r'goto'

t_IF = r'if'
t_INT = r'int'
t_LONG = r'long'
t_REGISTER = r'register'
t_RETURN = r'return'

t_SHORT = r'short'
t_SIGNED = r'signed'
t_SIZEOF = r'sizeof'
t_STATIC = r'static'
t_STRUCT = r'struct'

t_SWITCH = r'switch'
t_TYPEDEF = r'typedef'
t_UNION = r'union'
t_UNSIGNED = r'unsigned'
t_VOID = r'void'

t_ignore_VOLATILE = r'volatile'
t_WHILE = r'while'
t_ignore_DELSPEC = r'__delspec'
t_ignore_DLLIMPORT = r'dllimport'
t_ignore_DLLEXPORT = r'dllexport'

t_ELLIPSIS = r'\.\.\.'
t_RIGHT_ASSIGN = r'>>='
t_LEFT_ASSIGN = r'<<='
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='

t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'\/='
t_MOD_ASSIGN = r'%='
t_AND_ASSIGN = r'&='
t_XOR_ASSIGN = r'\^='

t_OR_ASSIGN = r'\|='
t_RIGHT_OP = r'>>'
t_LEFT_OP = r'<<'
t_INC_OP = r'\+\+'
t_DEC_OP = r'--'

t_PTR_OP = r'->'
t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_LE_OP = r'<='
t_GE_OP = r'>='

t_EQ_OP = r'=='
t_SUPER = r'super'

t_SEMI = r';'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = ','
t_LBRACK = r'\['
t_RBRACK = r'\]'

t_LP = r'\('
t_RP = r'\)'
t_COLON = r':'
t_ASSIGN = r'='
t_DOT = r'\.'
t_AND = r'&'

t_EXMARK = r'!'
t_WAVE = r'~'
t_SUB = r'-'
t_ADD = r'\+'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'%'
t_XOR = r'\^'
t_GE = r'>'
t_LE = r'<'
t_OR = r'\|'
t_QUESTION = r'\?'


t_IDENTIFIER = r'[a-zA-Z_]([a-zA-Z_]|[0-9])*'
t_HEX_CONSTANT = r'0[xX][a-fA-F0-9]+(u|U|l|L)*?'
t_OCT_CONSTANT = r'0[0-9]+(u|U|l|L)*?'
t_DEC_CONSTANT = r'[0-0]+(u|U|l|L)*?'

# D                      [0-9]
# L                      [a-zA-Z_]
# H                      [a-fA-F0-9]
# E                      [Ee][+-]?[0-9]+
# FS                      (f|F|l|L)
# IS                      (u|U|l|L)*

t_SCIENCE_COUNT = r'[0-9]+[Ee][+-]?[0-9]+?(f|F|l|L)'
t_DECIMAL = r'([0-9]*\.[0-9]+([Ee][+-]?[0-9]+)?(f|F|l|L)?)|([0-9]+\.[0-9]*([Ee][+-]?[0-9]+)?(f|F|l|L)?)'

t_OBJC_STRING = r'@\"(\\.|[^\\"])*\"'
t_C_STRING = r'\"(\\.|[^\\"])*\"'       # do not support 'L' expression to transform to an stack array

t_INTERFACE = r'@interface'
t_END = r'@end'


def t_error(t):
    print('Illegal character', t.value[0])
    t.lexer.skip(1)
