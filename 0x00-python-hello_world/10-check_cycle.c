#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list has a
 * cycle in it.
 * @list: pointer to a listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	if (list == NULL)
		return (0);

	while (1)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = (fast_ptr->next != NULL) ? fast_ptr->next->next : fast_ptr->next;

		if (fast_ptr == NULL)
			return (0);

		if (fast_ptr == slow_ptr)
			return (1);
	}
}
