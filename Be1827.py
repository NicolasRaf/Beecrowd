## Matriz Quadrada 4 ##

def creatMatriz(order):
    matriz = []

    for i in range(order):
        vector = []

        for j in range(order):
            value = 0
            vector.append(value)
        matriz.append(vector)

    return matriz

def fillDiagonals(matriz, order):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                matriz[i][j] = 2

            if i + j == (order - 1):
                matriz[i][j] = 3

def fillInternalPart(matriz, ordem):
    initial = ordem // 3
    final = ordem - ordem // 3 - 1
    
    for i in range(initial, final + 1):
        for j in range(initial, final + 1):
            matriz[i][j] = 1


def fillCenter(matriz,order):
    centerPosition = order // 2

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == centerPosition and j == centerPosition:
                matriz[i][j] = 4

def main():

    ## Processamento
    matriz = []
    vector = []

    while True:
        try:
            ## Entrada
            order = int(input())

            ## Processamento
            matriz = creatMatriz(order)

            fillDiagonals(matriz,order)
            fillInternalPart(matriz,order)
            fillCenter(matriz,order)

        ## Saída
            for line in matriz:
                print("".join(f"{num}" for num in line))
            print()

            matriz = []

        except EOFError:
            break

main()