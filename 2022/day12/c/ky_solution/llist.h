#ifndef LLIST_H
#define LLIST_H

typedef struct llist llist;
typedef struct llist_iter llist_iter;

llist *llist_create(void);

void llist_destroy(llist **list, void (*destroy)(void *));

int llist_enqueue(llist *list, void *data);

void *llist_dequeue(llist *list);

int llist_push(llist *list, void *data);

void *llist_pop(llist *list);

void *llist_peek(llist *list);

// Trick to allow you to iterate a llist at your convenience
// NOT THREAD SAFE!
llist_iter *llist_iter_create(llist *list);

void llist_iter_destroy(llist_iter **iter);

void *llist_iter_next(llist_iter *iter);

int llist_size(llist *list);

int llist_iter_size(llist_iter *iter);

#endif