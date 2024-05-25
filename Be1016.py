def main():
    #Entrada
    distancia = get_number()

    #Processamento
    tempo = distancia * 2


    #Saída
    print(f"{tempo} minutos")


def get_number():
    return int(input())


main()  