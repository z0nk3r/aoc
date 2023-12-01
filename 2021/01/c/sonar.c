#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

enum { MAX_BUFF = 64, MAX_LINE_LEN = 64, MAX_LINES = 2000, MAX_SUM = 7000};

int main(void) {

    typedef struct readings_s {
        long reading;
    } readings_s;

    FILE *f_input;
    const char *inputfile = "../input.txt";
    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}

    char line_buff[MAX_BUFF];
    int count = 0;
    char *trash;
    int flag_1 = 0, flag_2 = 0;
    long prev_read = 0, prev_sum = 0, cur_sum = 0;
    readings_s readings[MAX_LINES];

	while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        readings[count].reading = strtol(line_buff, &trash, 10);
        ++count;
    }

    //part 1
    for (int idx = 0; idx < MAX_LINES; ++idx) {
        // printf("read = %04ld, prev_read = %04ld\n", readings[idx].reading, prev_read);
        if ((readings[idx].reading > prev_read) && (prev_read != 0)) {
            flag_1++;
        }
        prev_read = readings[idx].reading;
    }

    //part 2
    for (int idx = 0; idx < MAX_LINES; ++idx) {
        cur_sum = readings[idx].reading + readings[idx+1].reading + readings[idx+2].reading;

        if ((cur_sum > prev_sum) && (prev_sum != 0) && !(cur_sum > MAX_SUM)){
            printf("%05d: cur_sum = %04ld, prev_sum = %04ld\n", idx, cur_sum, prev_sum);
            flag_2++;
        }
        else {
            printf("%05d: cur_sum = %04ld, prev_sum = %04ld (NOGO)\n", idx, cur_sum, prev_sum);
        }
        prev_sum = cur_sum;
    }

    printf("FLAG 1: %d\n", flag_1);
    printf("FLAG 2: %d\n", flag_2);
    fclose(f_input);


    // 1 NOT: 
    // 2 NOT: 1547(^)
}