## Menor e Posição ##

def main():
    ## Entrada
    size = int(input())
    numbers = input().split()

    ## Processamento
    vector = list(map( int,numbers))
    lowerValue = vector[0] 
    index = 0

    size = len(vector) if size > len(vector)  else size
    for i in range(size):
        if (vector[index] < lowerValue):
            lowerValue = vector[index]

        index += 1

    ## Saída
    print(f"Menor valor: {lowerValue}\nPosicao: {vector.index(lowerValue)}")

main()