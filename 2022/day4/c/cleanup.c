#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

enum { MAX_BUFF = 64, MAX_LINE_LEN = 64};

int main (void){

    FILE *f_input;
    const char *inputfile = "../input.txt";
    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}

    char line_buff[MAX_BUFF];
    const char *delims = "-,";
    int flag_1 = 0, flag_2 = 0;
    int elf1_lo = 0, elf1_hi = 0, elf2_lo = 0, elf2_hi = 0;

    // BUILD ALL RUCKS
	while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        elf1_lo = atoi(strtok(line_buff, delims));
        elf1_hi = atoi(strtok(NULL, delims));
        elf2_lo = atoi(strtok(NULL, delims));
        elf2_hi = atoi(strtok(NULL, delims));
        printf("[%02d:%02d] -> [%02d:%02d]", elf1_lo, elf1_hi, elf2_lo, elf2_hi);
        if (((elf1_lo >= elf2_lo) && (elf1_hi <= elf2_hi)) || ((elf2_lo >= elf1_lo) && (elf2_hi <= elf1_hi))){
            printf(" (flg_1 found) ");
            ++flag_1;
        } else {
            printf("               ");
        }
        if (((elf1_lo <= elf2_lo) && (elf1_hi >= elf2_lo)) || ((elf2_lo <= elf1_lo) && (elf2_hi >= elf1_lo))){
            printf("(flg_2 found)");
            ++flag_2;
        } else {
            printf("             ");
        }
        printf("\n");
    }
    printf("FLAG 1: %d\n", flag_1);
    printf("FLAG 2: %d\n", flag_2);
    fclose(f_input);

    return 0;

}