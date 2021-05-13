#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include "../include/takepic.h"

void rmspace(char *p){
    for (; *p; ++p){
        if (*p == ' ')
            *p = '_';
        if (*p == ':')
            *p = '-';
        if (*p == '\n')
            *p = '\0';
    }
}


char* takeshoot(char* dir){
    char path[50];
    char arg[50];

    time_t rawtime;

    time (&rawtime);
    sprintf(path,"%s/Figura_%s", dir, ctime(&rawtime));
    rmspace(path);
    strcat(path, ".jpg");
    strcpy(arg, "raspistill -o ");
    strcat(arg, path);
    printf("%s\n", arg);
    system(arg);
    char *str = malloc(50);
    str = path;
    return str;
}