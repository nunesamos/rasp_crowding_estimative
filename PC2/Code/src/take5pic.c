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
    char path[50];
    char arg[50];
    printf("Tudo bem até aqui\n");

    time_t rawtime;

    for(int i=0; i<Npic; i++){
        time (&rawtime);
        sprintf(path,"./pics/Figura_%s.jpg",ctime(&rawtime));
        rmspace(path);
        strcpy(arg, "raspistill -o ");
        strcat(arg, path);
        printf("%s\n", arg);
        system(arg);
    }

    return false;
}