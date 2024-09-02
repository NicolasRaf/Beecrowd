## Acima da Diagonal Principal ##
import random

def main():
    #Entrada
    operation = input().upper()

    #Processamento
    matriz = []
    vector = []
    result = 0
    soma = 0
    elementsAbove = 0

    for i in range(4):
        vector = []

        for j in range(4):
            vector.append(random.randint(0,50))   
        matriz.append(vector)

    for lineIndex in range(len(matriz)):
        currentLine = matriz[lineIndex]
        for columIndex in range(len(currentLine)):
            currentElement = currentLine[columIndex]

            if lineIndex < columIndex:
               elementsAbove += 1
               soma += currentElement
               result = soma if operation == "S" else soma/elementsAbove

    print(f"{result:.1f}")
    
main()