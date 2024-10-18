#include <stdio.h>
    
void checkCords(float *cords){
    if (cords[0] == 0.0 ){
        printf("Eixo X\n");
    }else if (cords[1] == 0.0){ 
        printf("Eixo Y\n");
    }else if (cords[0] == 0.0 && cords[1] == 0.0){
        printf("Origem\n");
    }else if(cords[0] > 0.0 && cords[1] > 0.0){
        printf("Q1\n");
    }else if (cords[0] < 0.0 && cords[1] > 0.0){
        printf("Q2\n");
    }else if (cords[0] < 0.0 && cords[1] < 0.0){
        printf("Q3\n");
    }else{
        printf("Q4\n");
    }
}   

int main(){
    float cords[2];
    scanf("%f %f", &cords[0], &cords[1]);

    checkCords(cords);
    return 0;
}