#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "../include/takepic.h"

int main(void){
    char dir[50] = "./pics";
    
    char *path = takeshoot(dir);


    printf("Tudo rodando: %s \n", path);

    return 0;
}