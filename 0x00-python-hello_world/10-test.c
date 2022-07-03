#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
	listint_t *current;
	listint_t *temp;
	listint_t *reset;
	int i;

	head = NULL;
	for (i = 0; i < 101; i++)
		add_nodeint(&head, i);

	print_listint(head);

	current = head;
	for (i = 0; i < 26; i++)
		current = current->next;
	temp = current;

	current = head;
	for (i = 0; i < 76; i++)
		current = current->next;
	reset = current->next;
	current->next = temp;

	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 76; i++)
		current = current->next;
	current->next = reset;

	free_listint(head);

	return (0);
}
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
	return (0);
}

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list of type listint_t
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}
/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
