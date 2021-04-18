#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include "../include/take5pic.h"

void rmspace(char *p){
    for (; *p; ++p){
        if (*p == ' ')
            *p = '_';
        if (*p == '\n')
            *p = '\0';
    }
}


bool takeLoopPic(){
    int Npic = 30;
    char Num[10] = "0";
    char path[50];
    char arg[50];
    printf("Tudo bem até aqui\n");

    time_t rawtime;

    for(int i=0; i<Npic; i++){
        time (&rawtime);
        sprintf(path,"./pics/Figura_%s",ctime(&rawtime));
        rmspace(path);
        strcat(path, ".jpg");
        strcpy(arg, "raspistill -o ");
        strcat(arg, path);
        printf("%s\n", arg);
        system(arg);
        sleep(54);
    }

    return false;
}