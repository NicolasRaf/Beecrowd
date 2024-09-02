## Área Superior ##

def main():
    #Entrada
    operation = input().upper()

    #Processamento
    matriz = []
    vector = []
    result = 0
    soma = 0
    elementsUpper = 0

    for i in range(144):
        vector.append(float(input()))

        if (i + 1) % 12 == 0:
            matriz.append(vector)
            vector = []

    for lineIndex in range(len(matriz)):
        currentLine = matriz[lineIndex]
        for columIndex in range(len(currentLine)):
            currentElement = currentLine[columIndex]

            if lineIndex + columIndex < 11 and lineIndex < columIndex:
               elementsUpper += 1
               soma += currentElement
               result = soma if operation == "S" else soma/elementsUpper

    print(f"{result:.1f}")
    
main()