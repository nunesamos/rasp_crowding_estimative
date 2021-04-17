#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include "../include/take5pic.h"

void rmspace(char *p){
    for (; *p; ++p){
        if (*p == ' ')
            *p = '_';
    }
}


bool takeLoopPic(){
    int Npic = 5;
    char Num[10] = "0";
    char arg[50];
    printf("Tudo bem até aqui\n");

    time_t rawtime;

    for(int i=0; i<Npic; i++){
        time (&rawtime);
        sprintf(arg,"raspistill -o ./pics/Figura_%s.jpg",ctime(&rawtime) );
        rmspace(arg);
        printf("%s\n", arg);
        system(arg);
    }

    return false;
}