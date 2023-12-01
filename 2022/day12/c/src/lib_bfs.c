#include "lib_bfs.h"

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>

struct vertex {
	char *id;
	int level;
	struct vertex *parent;
	llist_t *edges;
};

struct node_t {
	struct node_t *next;
	vertex *data;
};

struct llist_t {
	struct node_t *head;
	struct node_t *tail;
	uint64_t size;
};

/********************** LLIST FUNCS **********************/

// static void llist_delete_nodes(llist_t * llist);
static void llist_delete_nodes(llist_t * llist)
{
	struct node_t *node = llist->head;
	struct node_t *temp = NULL;

	while (node) {
		temp = node;
		node = node->next;

		destroy_vertex(temp->data);
		--llist->size;
		temp->data = NULL;
		temp->next = NULL;
		free(temp);
		temp = NULL;
	}
}

llist_t *llist_create()
{
	llist_t *llist = calloc(1, sizeof(*llist));

	return llist;
}

void llist_delete(llist_t ** p_llist)
{
	if (!p_llist) {
		return;
	}

	llist_delete_nodes(*p_llist);

	(*p_llist)->head = NULL;
	(*p_llist)->tail = NULL;
	free(*p_llist);
	*p_llist = NULL;
}


bool llist_enqueue(llist_t * llist, vertex * data)
{
	if (!llist || !data) {
		return false;
	}

	struct node_t *node = malloc(sizeof(*node));
	if (!node) {
		return false;
	}

	node->data = data;
	node->next = NULL;

	if (llist->tail) {
		llist->tail->next = node;
	} else {
		llist->head = node;
	}

	llist->tail = node;
	++llist->size;

	return true;
}

bool llist_dequeue(llist_t * llist, vertex ** data)
{
	bool ret = false;
	if (!data) {
		goto DEQUEUE;
	}
	// set to NULL in case of failure after verifying we can set to NULL
	*data = NULL;
	if (!llist) {
		goto DEQUEUE;
	}

	if (!llist->head) {
		goto DEQUEUE;
	}

	struct node_t *temp = llist->head;
	llist->head = temp->next;
	*data = temp->data;

	if (!llist->head) {
		llist->tail = NULL;
	}

	temp->next = NULL;
	temp->data = NULL;
	free(temp);
	temp = NULL;
	ret = true;
	--llist->size;

DEQUEUE:
	return ret;
}

bool llist_push(llist_t * llist, vertex * data)
{
	if (!llist || !data) {
		return false;
	}

	struct node_t *node = malloc(sizeof(*node));
	if (!node) {
		return false;
	}
	node->data = data;

	node->next = llist->head;
	llist->head = node;
	++llist->size;

	return true;
}

inline bool llist_pop(llist_t * llist, vertex ** data)
{
	return llist_dequeue(llist, data);
}

bool llist_is_empty(llist_t * llist)
{
	if (!llist) {
		return false;
	}
	return llist->size > 0 ? false : true;
}

uint64_t llist_get_size(llist_t * llist)
{
	if (!llist) {
		return 0;
	}
	return llist->size;
}

void llist_purge(llist_t * llist)
{
	if (!llist) {
		return;
	}

	struct node_t *node = llist->head;
	struct node_t *temp = NULL;
	while (node) {
		temp = node;
		node = node->next;
		free(temp);
	}
	llist->head = NULL;
	llist->tail = NULL;
}

vertex *llist_find(llist_t * llist, const char *id)
{
	vertex *data = NULL;
	struct node_t *node = llist->head;
	while (node) {
		if (is_match(node->data, id)) {
			data = node->data;
			break;
		}
		node = node->next;
	}
	return data;
}

void llist_print(llist_t * llist, int depth)
{
	if (!llist) {
		return;
	}

	struct node_t *node = llist->head;
	while (node) {
		print_vertex(node->data, depth);
		node = node->next;
	}
}

llist_t *llist_duplicate(llist_t * llist)
{
	llist_t *copy = llist_create();
	if (!copy) {
		return NULL;
	}

	struct node_t *node = llist->head;
	while (node) {
		llist_enqueue(copy, node->data);
		node = node->next;
	}
	return copy;
}

/********************** VERTEX FUNCS **********************/

vertex *create_vertex(const char *id)
{
	if (!id) {
		return NULL;
	}

	vertex *vertex = calloc(1, sizeof(*vertex));
	if (vertex) {
		vertex->id = strdup(id);
		vertex->edges = llist_create();
		vertex->level = INT_MAX;
		if (!vertex->edges) {
			free(vertex);
			vertex = NULL;
		}
	}
	return vertex;
}

// properly free custom_struct
//
void destroy_vertex(vertex * node)
{
	if (!node) {
		return;
	}

	llist_purge(node->edges);
	llist_delete(&(node->edges));
	free(node->id);
	free(node);
}

// compares custom_struct to string and answers if it is a match
//
bool is_match(vertex * node, const char *id)
{
	bool result = false;
	if (node && id) {
		if (0 == strcmp(node->id, id)) {
			result = true;
		}
	}

	return result;
}

// prints name of custom struct to stdout
//
void print_vertex(vertex * node, int depth)
{
	if (node) {
		if (depth) {
			printf("%s[%d]:", node->id, node->level);
			llist_print(node->edges, 0);
			printf("\n");
		} else {
			printf(" -> %s[%d]", node->id, node->level);
		}
	}
}

// returns -1 if thing1 < thing2
// returns 0 if thing1 == thing2
// returns 1 if thing1 > thing2
//
int compare_vertex(vertex * node_a, vertex * node_b)
{
	if (!node_a || !node_b) {
		return 0;
	}

	return strcmp(node_a->id, node_b->id);
}

void vertex_add_edge(vertex * node_a, vertex * node_b)
{
	if (!node_a || !node_b) {
		return;
	}

	llist_enqueue(node_a->edges, node_b);
}

struct llist_t *copy_edges(vertex * node)
{
	if (!node) {
		return NULL;
	}
	return llist_duplicate(node->edges);
}

void set_level(vertex * node, int level)
{
	if (!node) {
		return;
	}
	node->level = level;
}

int get_level(vertex * node)
{
	if (!node) {
		return -1;
	}
	return node->level;
}

char *get_id(vertex * node)
{
	if (!node) {
		return NULL;
	}
	return node->id;
}

void set_parent(vertex * node, vertex * parent)
{
	if (!node || !parent) {
		return;
	}
	node->parent = parent;
}

vertex *get_parent(vertex * node)
{
	if (!node) {
		return NULL;
	}
	return node->parent;
}
