#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

#define FILENAME "input"

// Custom Print Strings for shorthand message printing
#define pass(msg, ...) \
    printf("\033[1;32m[+]\033[0m " msg, ##__VA_ARGS__) // green bold
#define info(msg, ...) \
    printf("\033[1;34m[-]\033[0m " msg, ##__VA_ARGS__) // blue bold
#define warn(msg, ...) \
    printf("\033[1;33m[!]\033[0m " msg, ##__VA_ARGS__) // yellow bold
#define fail(msg, ...) \
    printf("\033[1;31m[x]\033[0m " msg, ##__VA_ARGS__) // red bold

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

    char   *line     = NULL;
    size_t  amt      = 0;
    ssize_t line_len = 0;

    int32_t length = 0;
    int32_t width  = 0;
    int32_t height = 0;

    while ((line_len = getline(&line, &amt, fp_input)) != EOF)
    {
        int32_t small_side = INT32_MAX;
        sscanf(line, "%dx%dx%d", &length, &width, &height);
        if ((length * width) < small_side)
        {
            small_side = length * width;
        }
        if ((length * height) < small_side)
        {
            small_side = length * height;
        }
        if ((width * height) < small_side)
        {
            small_side = width * height;
        }

        p1_retval
            += (2 * length * width + 2 * width * height + 2 * height * length);
        p1_retval += small_side;
    }
    free(line);

    info("Part 1 Results: %d\n", p1_retval);
    return p1_retval;
}

static int32_t
part2 (FILE *fp_input)
{
    int32_t p2_retval = 0;

    char   *line     = NULL;
    size_t  amt      = 0;
    ssize_t line_len = 0;

    int32_t length = 0;
    int32_t width  = 0;
    int32_t height = 0;

    while ((line_len = getline(&line, &amt, fp_input)) != EOF)
    {
        int32_t small_perim = INT32_MAX;
        sscanf(line, "%dx%dx%d", &length, &width, &height);
        if ((2 * length + 2 * width) < small_perim)
        {
            small_perim = 2 * length + 2 * width;
        }
        if ((2 * length + 2 * height) < small_perim)
        {
            small_perim = 2 * length + 2 * height;
        }
        if ((2 * width + 2 * height) < small_perim)
        {
            small_perim = 2 * width + 2 * height;
        }

        p2_retval += (length * width * height);
        p2_retval += small_perim;
    }
    free(line);

    info("Part 2 Results: %d\n", p2_retval);
    return p2_retval;
}
