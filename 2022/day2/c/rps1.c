#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

enum { MAX_BUFF = 64, MAX_LINE_LEN = 5};

int score_conv(char *player_char){
    player_char[strcspn(player_char, "\n")] = '\0';
    // printf("%s: ", player_char);
    if ((strncmp(player_char, "A", sizeof(char)) == 0) || (strncmp(player_char, "X", sizeof(char)) == 0)){
        // printf("Rock ");
        return 1;
    } else if ((strncmp(player_char, "B", sizeof(char)) == 0) || (strncmp(player_char, "Y", sizeof(char)) == 0)) {
        // printf("Paper ");
        return 2;
    } else if ((strncmp(player_char, "C", sizeof(char)) == 0) || (strncmp(player_char, "Z", sizeof(char)) == 0)){
        // printf("Scissors ");
        return 3;
    } else {
        printf("FALLTHRU >\n");
        return 0;
    }
}

int score_round(int opp, int you){
    // printf("\n");
    int score = 0;

    // win
    if ((opp == 3) && (you == 1)) {
        score = 6;
    }

    //lose
    else if ((opp == 1) && (you == 3)) {
        score = 0;
    }

    //win
    else if ((opp < you)){
        score = 6;
    }

    //draw
    else if (opp == you){
        score = 3;
    }

    //lose
    else if (opp > you){
        score = 0;
    }

    else {
        printf("FALLTHRU >\n");
    }
    int total = score+you;
    printf("Round result = s:%d + y:%d = %d\n", score, you, total);
    return total;
}

int main (void){

    FILE *f_input;
    char *inputfile = "../input.txt";
    if ((f_input = fopen(inputfile, "r")) == NULL) {
		perror("[!] fopen inputfile");
		exit(EXIT_FAILURE);
	}

    int flag = 0;
	char line_buff[MAX_BUFF];
    int round = 0;

	while (fgets(line_buff, MAX_LINE_LEN, f_input) != NULL) {
        char *opp_char = strtok(line_buff, " ");
        char *you_char = strtok(NULL, " ");
        printf("\nRound %d:\n", ++round);
        // printf("OPP_CHAR = %s, YOU_CHAR = %s", opp_char, you_char);
        flag += score_round(score_conv(opp_char), score_conv(you_char));
    }

    printf("FLAG 1 = %d\n", flag);
    fclose(f_input);

    return 0;

}