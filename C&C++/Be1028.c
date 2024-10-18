#include <stdio.h>

int main(){
    float value, prices[5] = {4.0, 4.5, 5, 2, 1.5};
    int choice, qtd;

    scanf("%d %d", &choice, &qtd);
    value = prices[choice - 1] * qtd;

    printf("Total: R$ %.2f\n", value);

    return 0;
}