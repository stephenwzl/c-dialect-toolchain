grammar Calculator;

expr : expr op=('*'|'/') expr     # MULDiv
     | expr op=('+'|'-') expr     # AddSub
     | INT                        # int
     | '(' expr ')'               # parens
     | op=('-'|'+') INT           # prehead1
     | op=('-'|'+') '(' expr ')'  # prehead2
     ;

INT  : [0-9]+;
MUL  : '*' ;
DIV  : '/' ;
ADD  : '+' ;
SUB  : '-' ;

WS   : [ \t\r\n]+ -> skip;