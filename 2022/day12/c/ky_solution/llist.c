#include <stdio.h>
#include <stdlib.h>
#include "llist.h"

struct llist_iter {
    void *data;
    struct llist_iter *next;
};

struct llist {
    llist_iter *head;
    llist_iter *tail;
    int size;
};

llist *llist_create(void)
{
    return calloc(1, sizeof(llist));
}

void llist_destroy(llist **list, void (*destroy)(void *))
{
    if (NULL == list || NULL == *list) {
        return;
    }

    llist_iter *current = (*list)->head;
    llist_iter *temp = NULL;
    while (current) {
        if (destroy) {
            destroy(current->data);
        }
        temp = current;
        current = current->next;
        free(temp);
    }
    free(*list);
    *list = NULL;
}

int llist_enqueue(llist *list, void *data)
{
    if (NULL == list || NULL == data) {
        return 0;
    }

    llist_iter *new = calloc(1, sizeof(*new));
    if (NULL == new) {
        return 0;
    }

    new->data = data;
    list->size++;
    if (NULL == list->tail) {
        list->head = new;
    } else {
        list->tail->next = new;
    }
    list->tail = new;
    return 1;
}

int llist_push(llist *list, void *data)
{
    if (NULL == list || NULL == data) {
        return 0;
    }

    llist_iter *new = calloc(1, sizeof(*new));
    if (NULL == new) {
        return 0;
    }

    if (NULL == list->tail) {
        list->tail = new;
    }
    new->next = list->head;
    new->data = data;
    list->head = new;
    list->size++;

    return 1;
}

void *llist_dequeue(llist *list)
{
    if (NULL == list || NULL == list->head) {
        return NULL;
    }

    llist_iter *temp = list->head;
    void *data = temp->data;

    list->head = temp->next;
    free(temp);

    if (NULL == list->head) {
        list->tail = NULL;
    }
    list->size--;
    return data;
}

void *llist_pop(llist *list)
{
    return llist_dequeue(list);
}

void *llist_peek(llist *list)
{
    if (NULL == list || NULL == list->head) {
        return NULL;
    }

    return list->head->data;
}

// neat struct trick for state tracking of linked list
// NOT THREAD SAFE!!!
llist_iter *llist_iter_create(llist *list)
{
    if (!list || !list->head) {
        return NULL;
    }

    llist_iter *iter = calloc(1, sizeof(*iter));
    if (NULL != iter) {
        iter->next = list->head;
    }

    return iter;
}

void llist_iter_destroy(llist_iter **iter)
{
    if (!iter || !*iter) {
        return;
    }
    free(*iter);
    *iter = NULL;
}

void *llist_iter_next(llist_iter *iter)
{
    if (!iter || !iter->next) {
        return NULL;
    }

    void *data = iter->next->data;
    iter->next = iter->next->next;

    return data;
}

int llist_iter_size(llist_iter *iter)
{
    if (!iter) {
        return -1;
    }
    int size = 0;

    llist_iter *node = iter->next;
    while (NULL != node) {
        size++;
        node = node->next;
    }

    return size;
}

int llist_size(llist *list)
{
    if (!list) {
        return -1;
    }

    return list->size;
}
