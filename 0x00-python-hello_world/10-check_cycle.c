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
	listint_t *temp, **current_addr, **next_addr, **tmp;
	unsigned int i = 1, j;

	temp = list;
	if (temp == NULL)
		return (0);
	current_addr = malloc(sizeof(char *) * (i + 1));
	*(current_addr + i) = NULL;
	*(current_addr + (i - 1)) = temp;
	temp = temp->next;
	while (temp != NULL)
	{
		j = 0;
		while (*(current_addr + j))
		{
			if (*(current_addr + j) == temp)
				return (1);
			j++;
		}
		++i;
		next_addr = malloc(sizeof(char *) * (i + 1));
		*(next_addr + i) = NULL;
		*(next_addr + (i - 1)) = temp;
		for (j = 0; *(current_addr + j); ++j)
			*(next_addr + j) = *(current_addr + j);
		tmp = current_addr;
		current_addr = next_addr;
		temp = temp->next;
		free(tmp);
	}
	free(current_addr);
	free(list);
	return (0);
}
