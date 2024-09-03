
def creatMatriz(N):
    matriz = []

    for _ in range(N):
        numbers = list(map(int,input().split()))
        matriz.append(numbers)

    return matriz


def verifyNeighbors(matriz,i,j):
    positionsArround = [
        matriz[i][j - 1],
        matriz[i][j + 1],
        matriz[i - 1][j],
        matriz[i + 1][j],
        matriz[i + 1][ j + 1],
        matriz[i - 1][ j - 1],
        matriz[i + 1][ j - 1],
        matriz[i - 1][ j + 1]
    ]

    for number in positionsArround:
        if int(number) != 7:
            return False
        
    return True

def foundSaber(matriz):

    for i in range(1, len(matriz) - 1):
        for j in range(1, len(matriz[i]) - 1):
            number = int(matriz[i][j])

            if number == 42 and verifyNeighbors(matriz,i,j):
                return (i + 1, j + 1)  
              
    return (0,0)
        
def main():
    ## Entrada
    N,M = map(int,input().split())
    matriz = creatMatriz(N)
    
    ## Processameto
    position = foundSaber(matriz)

    ## Saída
    print(f"{position[0]} {position[1]}")

main()