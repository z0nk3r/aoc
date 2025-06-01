#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#include "lib_hashtable.h"

#define FILENAME "input"

// Custom Print Strings for shorthand message printing
#define pass(msg, ...) printf("\033[1;32m[+]\033[0m " msg, ##__VA_ARGS__)  // green bold
#define info(msg, ...) printf("\033[1;34m[-]\033[0m " msg, ##__VA_ARGS__)  // blue bold
#define warn(msg, ...) printf("\033[1;33m[!]\033[0m " msg, ##__VA_ARGS__)  // yellow bold
#define fail(msg, ...) printf("\033[1;31m[x]\033[0m " msg, ##__VA_ARGS__)  // red bold

static int32_t part1(FILE *fp_input);
static int32_t part2(FILE *fp_input);
static void free_node(void *p_node);

int32_t
main (int argc, char **argv)
{
    (void)argc;
    (void)argv;

    FILE *fp_input = NULL;

    fp_input = fopen(FILENAME, "r");
    if (NULL == fp_input)
    {
        fail("Unable to open input file '%s'\n", FILENAME);
        return -1;
    }

    part1(fp_input);
    rewind(fp_input);
    part2(fp_input);

    (void)fclose(fp_input);

    return 0;
}

// =============================================================================
//                               STATIC FUNCTIONS
// =============================================================================

static int32_t
part1 (FILE *fp_input)
{
    int32_t p1_retval = 0;

    char    curr  = '\0';
    int64_t loc_r = 0;
    int64_t loc_c = 0;
    int64_t dir_r = 0;
    int64_t dir_c = 0;

    char curr_loc[50] = { 0 };

    htable_t *visited = ht_create(UINT16_MAX, 90);
    if (NULL == visited) {
        warn("ht_create failed");
        goto RESULTS;
    }

    snprintf(curr_loc, 50, "%ldx%ld", loc_r, loc_c);
    ht_insert(visited, curr_loc, (void *)0x12345);

    while ((curr = fgetc(fp_input)) != EOF)
    {
        if (curr == '^') {
            dir_r = -1;
            dir_c = 0;
        }
        else if (curr == '>') {
            dir_r = 0;
            dir_c = 1;
        }
        else if (curr == 'v') {
            dir_r = 1;
            dir_c = 0;
        }
        else if (curr == '<') {
            dir_r = 0;
            dir_c = -1;
        }
        
        memset(curr_loc, 0, 50);
        loc_r += dir_r;
        loc_c += dir_c;
        snprintf(curr_loc, 50, "%ldx%ld", loc_r, loc_c);
        ht_insert(visited, curr_loc, (void *)0x12345);
    }

    p1_retval = ht_size(visited);

 RESULTS:
    ht_destroy(visited, free_node);
    info("Part 1 Results: %d\n", p1_retval);
    return p1_retval;
}

static int32_t
part2 (FILE *fp_input)
{
    int32_t p2_retval = 0;

    char    curr     = '\0';
    int64_t sa_loc_r = 0;
    int64_t sa_loc_c = 0;
    int64_t rs_loc_r = 0;
    int64_t rs_loc_c = 0;
    int64_t dir_r    = 0;
    int64_t dir_c    = 0;
    int64_t ctr      = 0;

    char curr_loc[50] = { 0 };

    htable_t *visited = ht_create(UINT16_MAX, 90);
    if (NULL == visited) {
        warn("ht_create failed");
        goto RESULTS;
    }

    snprintf(curr_loc, 50, "%ldx%ld", sa_loc_r, sa_loc_c);
    ht_insert(visited, curr_loc, (void *)0x12345);

    while ((curr = fgetc(fp_input)) != EOF)
    {
        if (curr == '^') {
            dir_r = -1;
            dir_c = 0;
        }
        else if (curr == '>') {
            dir_r = 0;
            dir_c = 1;
        }
        else if (curr == 'v') {
            dir_r = 1;
            dir_c = 0;
        }
        else if (curr == '<') {
            dir_r = 0;
            dir_c = -1;
        }
        
        memset(curr_loc, 0, 50);
        if (ctr % 2 == 0) {
            sa_loc_r += dir_r;
            sa_loc_c += dir_c;
            snprintf(curr_loc, 50, "%ldx%ld", sa_loc_r, sa_loc_c);
        }
        else {
            rs_loc_r += dir_r;
            rs_loc_c += dir_c;
            snprintf(curr_loc, 50, "%ldx%ld", rs_loc_r, rs_loc_c);
        }
        ctr++;
        ht_insert(visited, curr_loc, (void *)0x12345);
    }

    p2_retval = ht_size(visited);

 RESULTS:
    ht_destroy(visited, free_node);

    info("Part 2 Results: %d\n", p2_retval);
    return p2_retval;
}

static void
free_node(void *p_node)
{
    // Do nothing
    ;
}