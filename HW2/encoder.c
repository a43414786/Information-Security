#include <stdio.h>
#include <stdlib.h>

void int2bin(int num,char bin[8]){
    for(int i = 0 ; i < 8 ; i++){
        bin[i] = 0;
    }
    for(int i = 7 ; i >= 0 ; i--){
        bin[i] = num % 2;
        num /= 2;        
    }
    return;
}

int bin2int(char bin[4]){
    
    int sum = 0;
    sum += 8 * bin[0];
    sum += 4 * bin[1];
    sum += 2 * bin[2];
    sum += bin[3];
    return sum;
}
int main(){
    char data[5][8];
    char rawData[5] = {'H','E','L','L','O'};
    for(int i = 0 ; i < 5 ; i++){
        int2bin(rawData[i],data[i]);
    }
    for(int j = 0 ; j < 5 ; j++){
        for(int i = 0 ; i < 8 ; i++){
            printf("%d",data[j][i]);
        }
        printf("\n");
    }
    printf("\n");

    char key[5][8];
    char rawKey[5] = {'S','E','C','R','E'};
    for(int i = 0 ; i < 5 ; i++){
        int2bin(rawKey[i],key[i]);
    }
    for(int j = 0 ; j < 5 ; j++){
        for(int i = 0 ; i < 8 ; i++){
            printf("%d",key[j][i]);
        }
        printf("\n");
    }
    printf("\n");

    char rst[5][8];
    for(int i = 0 ; i < 5 ; i++){
        int2bin(rawData[i] ^ rawKey[i],rst[i]);
    }
    for(int j = 0 ; j < 5 ; j++){
        for(int i = 0 ; i < 8 ; i++){
            printf("%d",rst[j][i]);
        }
        printf("\n");
    }
    printf("\n");

    printf("%c%c",'A' + bin2int(&(rst[0][0])),'A' + bin2int(&(rst[0][4])));
    printf("%c%c",'A' + bin2int(&(rst[1][0])),'A' + bin2int(&(rst[1][4])));
    printf("%c%c",'A' + bin2int(&(rst[2][0])),'A' + bin2int(&(rst[2][4])));
    printf("%c%c",'A' + bin2int(&(rst[3][0])),'A' + bin2int(&(rst[3][4])));
    printf("%c%c",'A' + bin2int(&(rst[4][0])),'A' + bin2int(&(rst[4][4])));

    return 0;
}
