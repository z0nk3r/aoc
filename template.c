#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define FILENAME "input"

// Custom Print Strings for shorthand message printing
#define pass(msg, ...) printf("\033[1;32m[+]\033[0m " msg, ##__VA_ARGS__)  // green bold
#define info(msg, ...) printf("\033[1;34m[-]\033[0m " msg, ##__VA_ARGS__)  // blue bold
#define warn(msg, ...) printf("\033[1;33m[!]\033[0m " msg, ##__VA_ARGS__)  // yellow bold
#define fail(msg, ...) printf("\033[1;31m[x]\033[0m " msg, ##__VA_ARGS__)  // red bold

static int32_t part1(FILE *fp_input);
static int32_t part2(FILE *fp_input);

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

    // solve part 1 of the problem here

    info("Part 1 Results: %d\n", p1_retval);
    return p1_retval;
}

static int32_t
part2 (FILE *fp_input)
{
    int32_t p2_retval = 0;

    // solve part 2 of the problem here

    info("Part 2 Results: %d\n", p2_retval);
    return p2_retval;
}

