#include <stdio.h>

char exam(avarage){
    float examNote;
}
  
char verifyStatus(avarage){
    if(avarage < 5){
        return "Aluno reprovado.";
    }
    else if (avarage >= 7){
        return "Aluno aprovado.";
    }

    return exam(avarage);
}

int main(){
    float notes[4], avarage;
    scanf("%f %f %f %f", &notes[0], &notes[1], &notes[2], &notes[3]);

    avarage += (notes[0] + notes[1] + notes[2] + notes[3]) /4;
    printf(verifyStatus(avarage));           
    
    return 0;
}