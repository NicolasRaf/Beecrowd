## Matriz Quadrada 2 ##

def main():
    ## Entrada
    order = int(input())

    ## Processamento
    matriz = []
    vector = []

    while order != 0:
        
        for i in range(order):
            vector = []
            for j in range(order):
                value = abs(i - j) + 1
                vector.append(value)
            matriz.append(vector)

        for line in matriz:
            ## Saída
            print(" ".join(f"{num:3}" for num in line))
        print()

        matriz = []
        order = int(input())

main()