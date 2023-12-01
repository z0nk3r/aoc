#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

enum { MAX_BUFF = 64, MAX_LINE_LEN = 20, MAX_ELVES = 270};

// https://stackoverflow.com/questions/13445845/easiest-to-use-int-array-sorting-function-in-c
int compare_int( const void* a, const void* b )
{
    if( *(int*)a == *(int*)b ) return 0;
    return *(int*)a > *(int*)b ? -1 : 1;
}

int main (void){

    FILE *f_input;
    char *inputfile = "../input.txt";
    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}

    //init the array
    long elves[MAX_ELVES];
    for (int idx = 0; idx < MAX_ELVES; ++idx) {
        elves[idx] = 0;
    }

    int flag = 0;
    int elf = 0;
    int idx_len = 0;
    int found_num = 0;
	char line_buff[MAX_BUFF];

    //build the array
	while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        char * a_number = strtok(line_buff, "\n");
        while(a_number != NULL){

            idx_len = 0;
            while (a_number[idx_len] != '\0'){
                ++idx_len;
            }

            // if just a newline
            if ((idx_len) <= 1){
                ++elf;
                // printf("[XXX] moving on to elf %d\n", elf);

            } else {
                sscanf(a_number, "%d", &found_num);
                elves[elf] += found_num;
                // printf("[!] Elf %d received %d\n", elf, found_num);
            }
            a_number = strtok(NULL, "\n");
        }
    }

    fclose(f_input);

    for (int idx = 0; idx < elf; ++idx) {
        // printf("Total calories of elf %d is: %ld\n", idx, elves[idx]);
        if (elves[idx] > flag) {
            flag = elves[idx];
        }
    }
    printf("\nFLAG 1: %d\n", flag);

    //
    //  part 2
    //
    flag = 0;
    qsort(elves, MAX_ELVES, sizeof(long), compare_int);

    for (int idx = 0; idx < 3; ++idx)
        flag += elves[idx];
    printf("FLAG 2: %d\n", flag);

    return 0;
}