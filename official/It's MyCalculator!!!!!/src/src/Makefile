cal: cal.l cal.y
	bison -d cal.y --verbose -Wcounterexamples
	flex cal.l
	gcc -o MyCalculator cal.tab.c lex.yy.c -lfl -fstack-protector

clean:
	rm -rf cal.tab*
	rm -rf lex.yy.c
	rm -rf MyCalculator
