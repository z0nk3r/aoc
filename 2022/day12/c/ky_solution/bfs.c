#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

#include "graph.h"

#define PRINT_SPEED 0.02 // in seconds

int main(int argc, char *argv[])
{
    int starter = 'S';
    double print_speed = PRINT_SPEED;
    int ret_code = 0;

    // TODO: getopt to get - option for starting letter, file, delay

    // TODO: if (argc < 2) {
    if (1 != argc) {
        fprintf(stderr, "%s requires a file to open\n", argv[0]);
        ret_code = 1;
        goto EXIT;
    }

    // TODO: FILE *fp = fopen(argv[1], "r");
    FILE *fp = fopen("input.txt", "r");
    if (NULL == fp) {
        perror("Fileopen failure");
        ret_code = 1;
        goto EXIT;
    }

    // TODO: add fileno/fstat for full validation
    // TODO: Validate file

    // 1's indexing
    int rows = 0;
    int cols = 0;

    // count rows and columns
    int letter = '\0';
    int col_ctr = 0;
    do {
        letter = fgetc(fp);
        ++col_ctr;
        if ('\n' == letter) {
            if (0 == cols) {
                cols = col_ctr;
            }
            ++rows;
        }
    } while (-1 != letter);

    // remove final of newline
    --cols;

    // put fp back to beginning
    rewind(fp);

    matrix *graph = graph_matrix_create(rows, cols);
    if (NULL == graph) {
        goto EXIT_FILE_CLOSE;
    }

    if (0 == graph_matrix_populate(graph, fp)) {
        fprintf(stderr, "File loading failed\n");
    }

    if (0 == graph_matrix_enrich(graph)) {
        fprintf(stderr, "Enrichment failed\n");
    }

    graph_matrix_bfs(graph);

    graph_matrix_best_start(graph, starter);

    graph_matrix_path_print(graph, print_speed);

    graph_matrix_destroy(&graph);

EXIT_FILE_CLOSE:
    fclose(fp);
EXIT:
    return ret_code;
}
