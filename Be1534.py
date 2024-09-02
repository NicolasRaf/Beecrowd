## Matriz 123 ##

def main():
    ## Entrada
    order = int(input())

    ## Processamento
    matriz = []
    vector = []

    while True:
        try:
            for i in range(order):
                vector = []
                for j in range(order):
                    if i + j == order - 1:
                        value = 2
                    elif i == j:
                        value = 1
                    else:
                        value = 3

                    vector.append(value)
                matriz.append(vector)

            for line in matriz:
                ## Saída
                print("".join(f"{num}" for num in line))

            matriz = []
            order = int(input())

        except EOFError:
            break

main()