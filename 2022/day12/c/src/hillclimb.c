#include "lib_bfs.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>
#include <strings.h>


typedef struct vertex {
	char id;
	int level;
	struct vertex* parent;
	struct edge* neighbors;
} vertex;

typedef struct edge {
	vertex *dest;
	struct edge* next;
} edge;

struct llist_t {
	struct edge* head;
	struct edge* tail;
	uint64_t size;
};

int add_edge(vertex* src, vertex* dest)
{
    int ret_code = 0;
    if (!src || !dest) {
        goto EXIT_ADD_EDGE;
    }

    edge* new_edge = calloc(1, sizeof(*new_edge));
    if (!new_edge) {
        //fprintf(stderr, "edge calloc failure");
        goto EXIT_ADD_EDGE;
    }

    new_edge->dest = dest;
    new_edge->next = src->neighbors;
    src->neighbors = new_edge;
    ret_code = 1;

EXIT_ADD_EDGE:
    return ret_code;
}

int main(void)
{

    FILE *fp = fopen("../input.txt", "r");
    if (!fp) {
        return -1;
    }
    int num_cols = 0;
    int num_rows = 0;
    char c = 0;
    while((c = fgetc(fp)) != EOF) { 
        ++num_cols;
        if (c == '\n') { 
            --num_cols;
            ++num_rows;
        }
    }
    num_cols = (num_cols / num_rows);
    // --num_rows;

    printf("rows x cols: %d %d\n", num_rows, num_cols);
    rewind(fp);

    llist_t* db = llist_create();
    if (!db) 
    {
        goto FILE_CLOSE;
        return -1;
    }
    vertex **matrix = calloc(num_rows, sizeof(*matrix));
    if (NULL == matrix) {
        perror("Matrix creation");
        goto FILE_CLOSE;
    }

    vertex *start = NULL;
    vertex *end = NULL;


    // create individual rows and populate each vertex with raw data
    for (int idx_row = 0; idx_row < num_rows; ++idx_row) {
        matrix[idx_row] = calloc(num_cols, sizeof(vertex));
        // TODO: ABC

        for (int idx_col = 0; idx_col < num_cols; ++idx_col) {
            c = fgetc(fp);

            switch (c)
            {
                case 'S':
                    start = matrix[idx_row] + idx_col;
                    printf("Found Start at %03d %03d\n", idx_row, idx_col);
                    c = 'a' - 1; // set start to be int correct
                    break;
                case 'E':
                    end = matrix[idx_row] + idx_col;
                    printf("Found End at %03d %03d\n", idx_row, idx_col);
                    c = 'z' + 1;
                    break;
            }

            matrix[idx_row][idx_col].id = c;
            matrix[idx_row][idx_col].level = INT_MAX;
        }

        // skip over newline we -- for earlier
        fgetc(fp);
    }
    // * return matrix_create() *



    // enrich_matrix(matrix, num_row, num_cols)
    // populates each nodes' neighbors if within tollerance

    //              N   E   S   W
    int mod_x[] = {-1,  0,  1,  0};
    int mod_y[] = { 0,  1,  0, -1};

    // for all rows
    vertex *neighbor = NULL;
    vertex *current = NULL;
    for (int i = 0; i < num_rows; ++i) {

        // for all columns
        for (int j = 0; j < num_cols; ++j) {
            current = &(matrix[i][j]);

            // for all cardinal directions
            for (int k = 0; k < 4; ++k) {
                int tgt_x = i + mod_x[k];
                int tgt_y = j + mod_y[k];

                // if destination in range
                if (-1 < tgt_x && tgt_x < num_rows && -1 < tgt_y && tgt_y < num_cols) {
                    neighbor = &(matrix[tgt_x][tgt_y]);

                    // and destination value acceptable
                    if (neighbor->id < current->id + 2) {

                        // add edge to current position
                        // printf("add edge current %c(%02x) (coord: {%03d, %03d})\n", current->id, current->id, i, j);
                        add_edge(current, neighbor);
                    }
                }
            }
        }
    }
    // * return enrich_matrix() *


    // TODO: BFS
    printf("[!] BFS Start\n");

    start->level = 0;

    // add start to queue
    llist_enqueue(db, end);
    // set start parent to start
    end->parent = end;

    vertex* node = end;
    // while stuff in queue: 
    while (llist_get_size(db) !=  0)
    {
        llist_dequeue(db, &node);
        llist_t* neighbors = node->neighbors;

        // early exit
        // if (node->id == start->id){
        //     break;
        // }

        // for each neighbor
        // for (int n = 0; n < 4; ++n)
        for(;;)
        {
            neighbor = neighbors->head;
            if (!neighbor){
                break;
            }

            // if neighbor not visited
            if (neighbor->parent == NULL) {
                // add neighbor to queue
                neighbor->parent = node;
                llist_enqueue(db, neighbor);
                // point neighbor to node 
                neighbor = neighbor->neighbors->next;
            }

        }
        // level ++
        node->level++;
    }

    node = end;
    printf("Shortest path is %03d turns.\n", node->level);
    while (node != node->parent)
    {

    //     push(node)
        printf("%c -> ", node->id);
        node = node->parent;
    }


EXIT_MATRIX:
    // TODO: matrix_destroy(&matrix);
    for (int i = 0; i < num_rows; ++i) {
        if (NULL != matrix[i]) {
            // TODO: Leaky. Must add support for each vertex's edges free'd
            free(matrix[i]);
        }
    }
    free(matrix);
    // *matrix_destroy()*

FILE_CLOSE:
    fclose(fp);
}