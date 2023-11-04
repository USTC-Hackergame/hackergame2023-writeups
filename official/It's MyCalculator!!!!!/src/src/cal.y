%{
#include <stdio.h>

extern int yylex();
void yyerror(const char * s);

#define MAX_RESULT_BUFFER 1024
int result_buffer[MAX_RESULT_BUFFER];
int result_buffer_index = 0;
%}

%token NUMBER
%token ADD SUB MUL DIV ABS
%token EOL
%token GET PUT '(' ')'

%left ADD SUB
%left MUL DIV

%%
calclist:
    | calclist exp EOL {
        result_buffer[result_buffer_index] = $2;
        printf("output = %d (Stored as idx %d)\n", $2, result_buffer_index);
        result_buffer_index++;
        result_buffer_index %= MAX_RESULT_BUFFER;
    }
    | calclist error EOL {
        printf("ignoring this line\n");
    }
    ;
exp:
      exp ADD term { $$ = $1 + $3; }
    | exp SUB term { $$ = $1 - $3; }
    | term
    ;
term:
      term MUL factor { $$ = $1 * $3; }
    | term DIV factor { if ($3 == 0) {yyerror("divide by zero");} else {$$ = $1 / $3;} }
    | factor
    ;
factor:
      NUMBER { $$ = $1; }
    | '(' exp ')' { $$ = $2; }
    | ABS factor { $$ = $2 >= 0 ? $2 : -$2; }
    | GET NUMBER {
        if ($2 >= MAX_RESULT_BUFFER) {
            yyerror("index out of range");
        } else {
            $$ = result_buffer[$2];
        }
    }
    | PUT NUMBER exp {
        if ($2 >= MAX_RESULT_BUFFER) {
            yyerror("index out of range");
        } else {
            result_buffer[$2] = $3;
            $$ = $3;
        }
    }
    ;
%%

int main(int argc, char **argv) {
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "error: %s\n", s);
}
