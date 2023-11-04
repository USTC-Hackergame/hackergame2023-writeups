%{
#include <stdio.h>
enum yytokentype {
    NUMBER = 258,
    ADD = 259,
    SUB = 260,
    MUL = 261,
    DIV = 262,
    ABS = 263,
    EOL = 264,
    GET = 265,
    PUT = 266,
};
extern int yylval;
%}

%%
"+"			{ return ADD; }
"-"			{ return SUB; }
"*" 		{ return MUL; }
"/" 		{ return DIV; }
"|" 		{ return ABS; }
[0-9]+		{ yylval = atoi(yytext); return NUMBER; }
\n 			{ return EOL; }
[ \t] 		{ /* ignore whitespace */ }
"GET"		{ return GET; }
"PUT"		{ return PUT; }
"("			{ return '('; }
")"			{ return ')'; }
.			{ printf("unknown char %c\n", *yytext); }
%%