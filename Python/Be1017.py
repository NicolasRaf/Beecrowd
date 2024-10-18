def main():
    #Entrada
    tempo = get_number()
    velocidade_media = get_number()

    #Processamento
    distancia = velocidade_media * tempo
    consumo = distancia/12

    #Saída
    print(f"{consumo:.3f}")


def get_number():
    return int(input())


main()  