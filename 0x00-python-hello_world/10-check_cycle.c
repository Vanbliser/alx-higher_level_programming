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
	listint_t *temp, *loop;
	unsigned int i = 0, j;

	temp = list;
	while (temp != NULL && temp->next != NULL)
	{
		loop = list;
		for (j = 0; j < i; ++j)
		{
			if (temp == loop)
				return (1);
			loop = loop->next;
		}
		temp = temp->next;
		++i;
	}
	return (0);
}
