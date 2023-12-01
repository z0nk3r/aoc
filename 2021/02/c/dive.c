#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

enum { MAX_BUFF = 64, MAX_LINE_LEN = 64, MAX_LINES = 1000};

int main(void) {


    FILE *f_input;
    const char *inputfile = "../input.txt";

    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}

    char line_buff[MAX_BUFF];
    char *trash;
    char *command;
    long flag_1 = 0, flag_2 = 0;
    long horiz = 0, depth = 0, aim = 0;
    int amount = 0, count = 0;

    while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        // commands[count].reading = strtol(line_buff, &trash, 10);
        command = strtok(line_buff, " ");
        amount = strtol(strtok(NULL, " "), &trash, 10);
        if (strncmp("forward", command, 8) == 0) {
            horiz += amount;
        } else if (strncmp("up", command, 8) == 0) {
            depth -= amount;
        } else if (strncmp("down", command, 8) == 0) {
            depth += amount;
        } else {
            printf("FALLLLLLTHRUUUUUUUU");
        }

        printf("%04d: horiz: %ld, depth: %ld (%s %d)\n", ++count, horiz, depth, command, amount);

    }

    flag_1 = horiz*depth;
    printf("\n======= FLAG 1: %ld =======\n\n", flag_1);
    fclose(f_input);

    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}
    
    horiz = 0, depth = 0, aim = 0, count = 0;
    while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        // commands[count].reading = strtol(line_buff, &trash, 10);
        command = strtok(line_buff, " ");
        amount = strtol(strtok(NULL, " "), &trash, 10);
        if (strncmp("forward", command, 8) == 0) {
            horiz += amount;
            depth += amount * aim;
        } else if (strncmp("up", command, 8) == 0) {
            aim -= amount;
        } else if (strncmp("down", command, 8) == 0) {
            aim += amount;
        } else {
            printf("FALLLLLLTHRUUUUUUUU");
        }

        printf("%04d: horiz: %ld, depth: %ld, aim: %ld (%s %d)\n", ++count, horiz, depth, aim, command, amount);

    }
    flag_2 = horiz*depth;
    printf("\n======= FLAG 2: %ld =======\n", flag_2);

    // 1982495697
}