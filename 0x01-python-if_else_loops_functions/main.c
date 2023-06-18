#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct structint
{
	int a;
	int b;
}strint;

void ch_ptr(strint *ptr);

int main()
{
	strint var;
	var.a = 5;
	var.b = 10;

	strint *b = &var;
	strint **c = &b;

	printf("var.a = %d\n", var.a);
	printf("b->a = %d\n", b->a);
	ch_ptr(b);
	printf("\n");
	printf("var.a = %d\n", var.a);
	printf("b->a = %d\n", b->a);
}

void ch_ptr(strint *ptr)
{
	ptr->a = 10;
}
