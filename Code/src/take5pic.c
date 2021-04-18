#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "../include/take5pic.h"


bool takeLoopPic(){
    int Npic = 30;
    char Num[10] = "0";
    char arg[50];
    printf("Tudo bem até aqui\n");

    for(int i=0; i<Npic; i++){
        
        strcpy(arg, "raspistill -o ./pics/Figura");
        sprintf(Num, "%d", i);
        strcat(arg,Num);
        strcat(arg,".jpg");
        printf("%s\n", arg);
        system(arg);
    }

    return false;
}