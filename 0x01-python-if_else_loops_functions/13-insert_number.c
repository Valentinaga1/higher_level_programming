#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to be inserted
 * Return: address of the newNode node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *temp;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;
	temp = (*head);

	if (temp == NULL)
	{
		newNode->next = (*head);/*se inserta al inicio. head apuntaría a new*/
		/*y new apuntaría a donde estaba apuntando head*/
		(*head) = newNode;
		return (newNode);
	}
	while (temp->next->n < number)
	{
		temp = temp->next;
		if (temp == NULL)
			return (NULL);
	}
		newNode->next = temp->next;
		temp->next = newNode;
		/*Ejm idx 3:temp next apunta a n2 y n2 apunta a newnode y new node apunta*/
		/*al que era n3*/
	return (newNode);
}