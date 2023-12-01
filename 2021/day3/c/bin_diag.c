#include <math.h>
#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

enum { MAX_BUFF = 64, MAX_LINE_LEN = 64, MAX_COLS = 12}; //5 for smol

int bintodec(char *input_string) {
    int answer = 0;
    char *trash;
    size_t string_len = strlen(input_string);

    for (int i = 0; i < MAX_COLS; ++i) {
        // printf("%d %d %ld %d\n", input_string[i], (input_string[i]-'0'), string_len, (int) (pow(2, string_len)));
        answer += (input_string[i]-'0')*((int) (pow(2, string_len)));
        --string_len;
        // printf("answer %d", answer);
    }
    return answer/2;
}

int main(void) {

    typedef struct counter_s {
        long zero_count;
        long one_count;
    } counter_s;

    FILE *f_input;
    const char *inputfile = "../input.txt";
    // const char *inputfile = "../input_smol.txt";

    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}

    char gamma_ans[MAX_COLS+1];
    char line_buff[MAX_BUFF];
    counter_s counters[MAX_COLS];
    char epsi_ans[MAX_COLS+1];

    // init all counters
    for (int idx = 0; idx < MAX_COLS; ++idx) {
        counters[idx].zero_count = 0;
        counters[idx].one_count = 0;
    }

    while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        for (size_t idx = 0; idx < strlen(line_buff); ++idx) {
            if (line_buff[idx] == '0') {
                counters[idx].zero_count++;
            } else if (line_buff[idx] == '1') {
                counters[idx].one_count++;
            } else {
                ;
            }
        }
    }

    fclose(f_input);

    for (int idx_counter = 0; idx_counter < MAX_COLS; idx_counter++) {
        if (counters[idx_counter].zero_count > counters[idx_counter].one_count) {
            gamma_ans[idx_counter] = '0';
            epsi_ans[idx_counter] = '1';
        } else {
            gamma_ans[idx_counter] = '1';
            epsi_ans[idx_counter] = '0';
        }
    }

    gamma_ans[MAX_COLS] = '\0';
    epsi_ans[MAX_COLS] = '\0';

    printf("Gamma Rate: %s (%d) \n", gamma_ans, bintodec(gamma_ans));
    printf("Epsilon Rate: %s (%d)\n", epsi_ans, bintodec(epsi_ans));

    printf("FLAG 1: %d\n", bintodec(gamma_ans)*bintodec(epsi_ans));
}
