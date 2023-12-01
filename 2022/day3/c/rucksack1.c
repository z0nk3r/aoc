#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

enum { MAX_BUFF = 64, MAX_LINE_LEN = 55};

char find_match(char *ruck_a, char *ruck_b){
    for (size_t a_idx = 0; a_idx < strlen(ruck_a); ++a_idx) {
        for (size_t b_idx = 0; b_idx < strlen(ruck_b); ++b_idx) {
            if (ruck_a[a_idx] == ruck_b[b_idx]) {
                return ruck_a[a_idx];
            }
        }
    }
    return 'a';
}

int score_match(char found_match) {
    // printf("\n\t\tFound match: %d\n", found_match);
    int match_score = 0;

    if (found_match > 95) {
        match_score = (int) (found_match-96);
    }
    else {
        match_score = (int) (found_match-38);
    }

    printf("\tFound: '%c' Score: %d\n", found_match, match_score);
    return match_score;
}

int main (void){

    FILE *f_input;
    const char *inputfile = "../input.txt";
    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}

    int flag = 0;
	char line_buff[MAX_BUFF];
    int round = 0;

	while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        size_t half_buff = ((strlen(line_buff)-1)/2);

        char ruck_a[half_buff+1];
        char ruck_b[half_buff+1];

        ruck_a[half_buff] = '\0';
        ruck_b[half_buff] = '\0';

        for (size_t idx = 0; idx < half_buff; ++idx) {
            ruck_a[idx] = line_buff[idx];
        }
        for (size_t idx = 0; idx < (strlen(line_buff)/2); ++idx) {
            ruck_b[idx] = line_buff[idx+(strlen(line_buff)-1)/2];
        }

        printf("Line %03d: (%ld) a:%s b:%s\n", ++round, strlen(line_buff), ruck_a, ruck_b);
        // // printf("OPP_CHAR = %s, YOU_CHAR = %s", opp_char, you_char);

        flag += score_match(find_match(ruck_a, ruck_b));

    }

    printf("\nFLAG 1 = %d\n", flag);
    fclose(f_input);

    return 0;

}