#include "lists.h"

/**
 * insert_node -  a function in C that inserts a number into a
 * sorted singly linked list.
 * @head: pointer to a pointer to a listint_t
 * @number: an integer
 *
 * Return: pointer to the inserted value
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *tmp, *new;

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	else if ((*head)->n > new->n)
	{
		current = *head;
		*head = new;
		new->next = current;
		return (new);
	}
	else if ((*head)->next == NULL)
	{
		(*head)->next = new;
		return (new);
	}
	else
	{
		current = *head;
		while (current->next)
		{
			if (current->next->n > new->n)
			{
				tmp = current->next;
				current->next = new;
				new->next = tmp;
				return (new);
			}
			current = current->next;
		}
		current->next = new;
	}
	return (new);
}
