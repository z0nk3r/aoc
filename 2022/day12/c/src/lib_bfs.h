/*
*
* Lib containing both LLIST and Vertex functions for a BFS 
*
*/

#ifndef LIB_BFS_H
#define LIB_BFS_H
#include <stdbool.h>
#include <stdint.h>

typedef struct llist_t llist_t;

typedef struct vertex vertex;

/* Linked List Funcs */

/**
 * @brief Allocates linked-list
 * 
 * @return llist_t* On success, NULL on failure 
 */
llist_t *llist_create();
/**
 * @brief Function to delete linked list and free memory
 * 
 * @param p_llist Linked-list to delete
 */
void llist_delete(llist_t **p_llist);
/**
 * @brief Adds void* to linked-list as a queue
 * 
 * @param llist Linked-list to enqueue() to
 * @param data custom_thing to be added
 * @return true On success
 * @return false On failure
 */
bool llist_enqueue(llist_t *llist, vertex *data);
/**
 * @brief Removes void* from linked-list as a queue
 * 
 * @param llist Linked-list to dequeue() from
 * @param data custom_thing** pointer of place to store data pointer to
 * @return true On success
 * @return false On failure
 */
bool llist_dequeue(llist_t *llist, vertex **data);
/**
 * @brief Adds void* to linked-list as a stack
 * 
 * @param llist Linked-list to push() to
 * @param data custom_struct to be added to linked-list
 * @return true On success
 * @return false On failure
 */
bool llist_push(llist_t *llist, vertex *data);
/**
 * @brief Removes void* from linked-list as a stack
 * 
 * @param llist Linked-list to pop() from
 * @param data custom_struct** pointer of place to store data pointer to
 * @return true On success
 * @return false On failure
 */
bool llist_pop(llist_t *llist, vertex **data);
/**
 * @brief Checks if linked-list is empty
 * 
 * @param list Linked-list to check
 * @return true Is empty
 * @return false Not empty
 */
bool llist_is_empty(llist_t *llist);
// Emptys linked list without doing anything to stored pointers
//
void llist_purge(llist_t *llist);
uint64_t llist_get_size(llist_t *llist);
vertex *llist_find(llist_t *llist, const char *id);
void llist_print(llist_t *llist, int depth);
llist_t *llist_duplicate(llist_t *llist);

/* Vertex Funcs */

// name to be used as some sort of token
//
vertex *create_vertex(const char *id);
// properly free custom_struct
//
void destroy_vertex(vertex *node);
// compares custom_struct to string and answers if it is a match
//
bool is_match(vertex *node, const char *word);
// prints name of custom struct to stdout
//
void print_vertex(vertex *node, int depth);
// returns -1 if thing1 < thing2
// returns 0 if thing1 == thing2
// returns 1 if thing1 > thing2
//
int compare_vertex(vertex *node_a, vertex *node_b);
void vertex_add_edge(vertex *node_a, vertex *node_b);
struct llist_t *copy_edges(vertex *node);
void set_level(vertex *node, int level);
int get_level(vertex *node);
char *get_id(vertex *node);
void set_parent(vertex *node, vertex *parent);
vertex *get_parent(vertex *node);

#endif