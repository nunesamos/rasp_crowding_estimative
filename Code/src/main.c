#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "../include/takepic.h"

int main(int argc, char **argv){

    int N = *argv[1] - '0';
    char dir[50] = "./pics";
    char arg[100];

    for(int i=0; i < N; i++){
  
        char *path = takeshoot(dir); // Tira uma foto

        strcpy(arg, "cd build; ./sample/crwd_fd ../data/models .");
        strcat(arg, path);

        system(arg);
    }
    return 0;
}