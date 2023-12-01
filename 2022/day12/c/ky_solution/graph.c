#define _DEFAULT_SOURCE
#include <limits.h>
#include <stdlib.h>
#include <time.h>

#include "graph.h"

#define CURSER_MOVE "\033[%d;%dH"

#define RED "\033[31m"
#define GREEN "\033[32m"
#define RESET "\033[0m"
#define YELLOW "\033[33m"
#define CLEAR_SCREEN "\033[2J\033[;H"
#define HIDE_CURSOR "\033[?25l"
#define TIME_MODIFIER 1000000000L // 1 second in nano

typedef struct vertex {
    struct vertex *parent;
    llist *neighbors;
    char id;
    int x;
    int y;
} vertex;

struct matrix {
    vertex **grid;
    vertex *start;
    vertex *end;
    llist *list;
    int rows;
    int cols;
};

static int add_edge(llist *list, vertex *dest);

static void grid_destroy_row(vertex *row, int cols);

static void grid_destroy(vertex **grid, int rows, int cols);

static int grid_create_row(vertex **row, int cols);

static int route_length(vertex *node, vertex *destination);


static int add_edge(llist *list, vertex *dest)
{
    int ret_code = 1;
    if (!list || !dest) {
        ret_code = 0;
        goto EXIT_ADD_EDGE;
    }

    if (0 == llist_enqueue(list, dest)) {
        fprintf(stderr, "enqueue failed\n");
        ret_code = 0;
    }

EXIT_ADD_EDGE:
    return ret_code;
}

static void grid_destroy_row(vertex *row, int cols)
{
    if (!row) {
        return;
    }
    for (int col = 0; col < cols; ++col) {
        if (NULL != row[col].neighbors) {
            llist_destroy(&(row[col].neighbors), NULL);
        }
    }
    free(row);
}

static void grid_destroy(vertex **grid, int rows, int cols)
{
    if (NULL == grid) {
        return;
    }

    for (int row = 0; row < rows; ++row) {
        grid_destroy_row(grid[row], cols);
    }
    free(grid);
}

void graph_matrix_destroy(matrix **graph)
{
    if (NULL == graph || NULL == *graph) {
        return;
    }
    grid_destroy((*graph)->grid, (*graph)->rows, (*graph)->cols);
    llist_destroy(&((*graph)->list), NULL);
    free(*graph);
    *graph = NULL;
}

static int grid_create_row(vertex **row, int cols)
{
    int ret_val = 0;
    *row = calloc(cols, sizeof(vertex));
    if (NULL != *row) {
        for (int col = 0; col < cols; ++col) {
            (*row)[col].neighbors = llist_create();
            if (NULL == (*row)->neighbors) {
                break;
            }
        }
        ret_val = 1;
    }

    return ret_val;
}

matrix *graph_matrix_create(int rows, int cols)
{
    if (rows < 1 || cols < 1) {
        return NULL;
    }
    // create wrapper
    matrix *graph = calloc(1, sizeof(*graph));
    if (NULL != graph) {
        graph->rows = rows;
        graph->cols = cols;

        // create rows array
        graph->grid = calloc(rows, sizeof(vertex *));
        if (NULL != graph->grid) {

            // create columns arrays
            for (int row = 0; row < rows; ++row) {
                grid_create_row(graph->grid + row, cols);

                if (NULL == graph->grid + row) {
                    grid_destroy(graph->grid, rows, cols);
                    free(graph);
                    graph = NULL;
                    break;
                }
            }
        }
    }
    graph->list = llist_create();
    if (NULL == graph->list) {
        grid_destroy(graph->grid, rows, cols);
        free(graph);
        graph = NULL;
    }

    return graph;
}

int graph_matrix_populate(matrix *graph, FILE *fp)
{
    if (!graph || !fp) {
        return 0;
    }

    for (int row = 0; row < graph->rows; ++row) {
        for (int col = 0; col < graph->cols; ++col) {
            vertex *node = graph->grid[row] + col;
            int letter = fgetc(fp);

            switch (letter)
            {
                case 'S':
                    graph->start = node;
                    break;
                case 'E':
                    graph->end = node;
                    break;
            }

            node->id = letter;
            node->x = row;
            node->y = col;
        }
        // clears new line, assumes columns populated correctly
        fgetc(fp);
    }

    return 1;
}

int graph_matrix_enrich(matrix *graph)
{
    if (!graph) {
        return 0;
    }
    int mod_x[] = {-1, 0, 1,  0};
    int mod_y[] = { 0, 1, 0, -1};
    int rows = graph->rows;
    int cols = graph->cols;

    graph->start->id = 'a' - 1;
    graph->end->id = 'z' + 1;

    // for each row
    for (int row = 0; row < rows; ++row) {

        // for each column
        for (int col = 0; col < cols; ++col) {
            vertex *current = graph->grid[row] + col;

            // for each direction from current position
            for (int dir = 0; dir < 4; ++dir) {
                int nei_x = row + mod_x[dir];
                int nei_y = col + mod_y[dir];

                // if neighbor not out of matrix range
                if (-1 < nei_x && nei_x < rows && -1 < nei_y && nei_y < cols) {
                    vertex *neighbor = graph->grid[nei_x] + nei_y;

                    // if neighbor id within tollerance
                    if (neighbor->id > current->id - 2) {
                        add_edge(current->neighbors, neighbor);
                    }
                }
            }
        }
    }
    graph->start->id = 'S';
    graph->end->id = 'E';
    return 1;
}

void graph_matrix_bfs(matrix *graph)
{
    llist *list = graph->list;
    vertex *end = graph->end;

    // add start to queue
    end->parent = end;
    llist_enqueue(list, end);

    // while queue not empty
    while (0 != llist_size(list)) {

        // extract item from queue
        vertex *current = llist_dequeue(list);

        llist_iter *neighbors = llist_iter_create(current->neighbors);
        if (NULL == neighbors) {
            fprintf(stderr, "No neighbors\n");
        }

        // for neighbor in neighbors
        for (;;) {
            vertex *neighbor = llist_iter_next(neighbors);
            if (!neighbor) {
                break;
            }

            // if neighbor not discovered
            if (NULL == neighbor->parent) {

                // add neighbor to queue
                neighbor->parent = current;
                llist_enqueue(list, neighbor);
            }
        }
        // free up the current neighbors iter
        llist_iter_destroy(&neighbors);
    }
}

void graph_matrix_print(matrix *graph)
{
    if (NULL == graph) {
        return;
    }

    vertex *start = graph->start;
    vertex *end = graph->end;
    int rows = graph->rows;
    int cols = graph->cols;

    printf(CLEAR_SCREEN);
    printf(HIDE_CURSOR);
    printf(GREEN);
    for (int row = 0; row < rows; ++row) {
        for (int col = 0; col < cols; ++col) {
            vertex *node = graph->grid[row] + col;
            if (node == start || node == end) {
                printf(YELLOW);
            }
            fputc(node->id, stdout);
            if (node == start || node == end) {
                printf(GREEN);
            }
        }
        fputc('\n', stdout);
    }
    printf(RESET);
}

void graph_matrix_path_print(matrix *graph, double delay)
{
    if (NULL == graph || graph->end->parent != graph->end) {
        return;
    }
    graph_matrix_print(graph);

    struct timespec tm = { 0 };
    tm.tv_sec = 0;
    tm.tv_nsec = TIME_MODIFIER * delay;

    printf(RED);
    vertex *temp = graph->start;
    for (;;) {
        temp = temp->parent;
        vertex *next = temp->parent;
        if (temp == next) {
            break;
        }

        char direction = '\0';
        if (temp->y == next->y) {
            direction = temp->x < next->x ? 'v' : '^';
        } else {
            direction = temp->y < next->y ? '>' : '<';
        }
        printf(CURSER_MOVE, temp->x + 1, temp->y + 1);
        fputc(direction, stdout);
        fflush(stdout);

        nanosleep(&tm, NULL);
    }
    printf(RESET);
    printf(CURSER_MOVE, graph->rows + 1, 1);
    int steps = route_length(graph->start, graph->end);
    printf("We took %d steps.\n", steps);
}

static int route_length(vertex *node, vertex *destination)
{
    if (NULL == node || NULL == destination) {
        return 0;
    }

    int steps = 0;
    for (;;) {
        steps++;
        // move forward 1 so verticies == edges
        node = node->parent;
        if (NULL == node) {
            steps = 0;
            break;
        }
        if (node == destination) {
            break;
        }
    }
    return steps;
}

void graph_matrix_best_start(matrix *graph, int letter)
{
    if (!graph || letter < 'a' || 'z' < letter) {
        return;
    }
    int best_route = INT_MAX;

    for (int row = 0; row < graph->rows; ++row) {
        for (int col = 0; col < graph->cols; ++col) {
            vertex *node = graph->grid[row] + col;
            if (letter == node->id) {
                int steps = route_length(node, graph->end);
                if (0 < steps && steps < best_route) {
                    graph->start = node;
                    best_route = steps;
                }
            }
        }
    }
}