## Matriz Quadrada 3 ##

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
                value = 2 ** (j + i)
                vector.append(value)

    
            matriz.append(vector)
            
        # Encontrar o maior valor na matriz para determinar o espaçamento
        maxValue = matriz[-1][-1]
        T = len(str(maxValue))

       ## Saída
        for line in matriz:
            print(" ".join(f"{num:>{T}}" for num in line))
        print()

        matriz = []
        order = int(input())

main()