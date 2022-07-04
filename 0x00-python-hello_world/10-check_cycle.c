#include "lists.h"
/**
 * check_cycle - a function in C that checks if a singly linked list
 * has a cycle in it.
 * Only these functions are allowed: write, printf, putchar, puts, malloc, free
 * @list: a pointer to the singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *step2;

	step2 = list;
	while (list && step2 && step2->next)
	{
		list = list->next;
		step2 = step2->next->next;
		if (list == step2)
			return (1);
	}
	return (0);
}
