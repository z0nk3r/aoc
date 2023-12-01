#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

enum { MAX_BUFF = 64, MAX_LINE_LEN = 55, MAX_RUCKS = 301};

typedef struct all_rucks {
	char string[MAX_BUFF];
} all_rucks;

int score_match(char found_match) {
    // printf("\n\t\tFound match: %d\n", found_match);
    int match_score = 0;

    if (found_match > 95) {
        match_score = (int) (found_match-96);
    }
    else {
        match_score = (int) (found_match-38);
    }

    printf("\tFound: '%c' Score: %d\n\n", found_match, match_score);
    return match_score;
}

void find_matches(int num_rucks, all_rucks *rucks){
    long flag = 0;
    bool first_check = true;
    for (int idx = 0; idx <= num_rucks; ++idx) {
        printf("1: %s \n2: %s \n3: %s\n", rucks[idx].string, rucks[idx+1].string, rucks[idx+2].string);
        for (size_t a_idx = 0; a_idx < strlen(rucks[idx].string); ++a_idx) {
            for (size_t b_idx = 0; b_idx < strlen(rucks[idx+1].string); ++b_idx) {
                for (size_t c_idx = 0; c_idx < strlen(rucks[idx+2].string); ++c_idx) {
                    // if a == b, b == c, and a == c
                    if ((rucks[idx].string[a_idx] == rucks[idx+1].string[b_idx]) && (rucks[idx+1].string[b_idx] == rucks[idx+2].string[c_idx]) && first_check) { 
                        flag += score_match(rucks[idx].string[a_idx]);
                        first_check = false;
                    }
                }
            }
        }
        ++idx;
        ++idx;
        first_check = true;
    }
    printf("\nFLAG 2 = %ld\n", flag);
}

int main (void){

    FILE *f_input;
    const char *inputfile = "../input.txt";
    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}

    all_rucks rucks[MAX_RUCKS];

    // long flag = 0;
	char line_buff[MAX_BUFF];
    int round = 0;

    // BUILD ALL RUCKS
	while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        char a_ruck[MAX_BUFF];

        for (size_t idx = 0; idx < strlen(line_buff); ++idx) {
            a_ruck[idx] = line_buff[idx];
        }

        a_ruck[strcspn(a_ruck, "\n")] = '\0';

        strncpy(rucks[round].string, a_ruck, MAX_BUFF);
        ++round;

    }

    find_matches(round-1, rucks);
    fclose(f_input);

    return 0;

}