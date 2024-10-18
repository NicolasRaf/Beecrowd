## Acima da Diagonal Principal ##

def main():
    #Entrada
    operation = input().upper()

    #Processamento
    matriz = []
    result = 0
    soma = 0
    elementsAbove = 0

    for i in range(12):
        vector = []

        for j in range(12):
            vector.append(float(input()))

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