#ifndef GRAPH_H
#define GRAPH_H

#include <stdio.h>
#include "llist.h"

typedef struct matrix matrix;

matrix *graph_matrix_create(int rows, int cols);

void graph_matrix_destroy(matrix **graph);

int graph_matrix_populate(matrix *graph, FILE *fp);

int graph_matrix_enrich(matrix *graph);

void graph_matrix_bfs(matrix *graph);

void graph_matrix_path_print(matrix *graph, double delay);

void graph_matrix_best_start(matrix *graph, int letter);


#endif