#include <stdio.h>

void exam(float avarage){
    float examNote = 0.0;
    scanf("%f", &examNote);

    printf("Media: %.1f\n", avarage);
    printf("Aluno em exame.\n");    
    avarage = (avarage + examNote)/2;

    printf("Nota do exame: %.1f\n", examNote);

    if(avarage < 5){
        printf("Aluno reprovado.\n");
    }else{
        printf("Aluno aprovado.\n");
    }

    printf("Media final: %.1f\n", avarage);
}
  
void verifyStatus(float avarage){
    if(avarage < 5){
        printf("Media: %.1f\n", avarage);
        printf("Aluno reprovado.\n");

        return;
    }
    else if (avarage >= 7){
        printf("Media: %.1f\n", avarage);
        printf("Aluno aprovado.\n");
        return;
    }

    exam(avarage);
}

int main(){
    float notes[4], avarage = 0.0;
    scanf("%f %f %f %f", &notes[0], &notes[1], &notes[2], &notes[3]);

    avarage += ((notes[0] * 2.0) + (notes[1] * 3.0) + (notes[2] * 4.0) + notes[3]) / 10.0;
    verifyStatus(avarage);         
    
    return 0;
}