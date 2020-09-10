#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_listint - Function that reverses a listint_t linked list.
 * @head:Pointer to pointer to the first element of a linked list.
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *cur;

	if ((*head) == NULL)
		return (NULL);
	if ((*head) != NULL)
	{
		prev = (*head);
		cur = (*head)->next;
		(*head) = (*head)->next;
	}
	prev->next = NULL;/*el primer nodo será el último nodo*/
	while ((*head) != NULL)
	{
		(*head) = (*head)->next;
		cur->next = prev;/*se conencta el nodo actual con prev*/
		prev = cur;
		cur = (*head);/*nodo prev al actual y actual a head*/
	}
	(*head) = prev;/*se hace head el último nodo*/

	return (prev);
}
int is_palindrome(listint_t **head)
{
	listint_t *a, *b;
	int len = 0, i = 0;

	a = *head;
	b = *head;

	while (a != NULL)
	{
		a = a->next;
		len++;/*len de la linked list*/
	}

	while (i < len / 2)
	{
		b = b->next;/*b va de head a la mitad de la linked list*/
		i++;/*b avanza i veces hasta legar a la mitad*/
	}
	reverse_listint(&b);/*reverso la lista de la mitad hasta el fin*/
	a = *head;/*reinicio a*/
	/*recorro la lista desde head(a) y la mitad reversada(b)*/
	while (a != NULL && b != NULL)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}
	return (1);
}
