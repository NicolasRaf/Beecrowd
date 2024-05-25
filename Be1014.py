def main():
    #Entrada
    distancia = get_number()
    combustível_gasto = get_float_number()

    #Processamento
    consumo = distancia/combustível_gasto

    #Saída
    print(f"{consumo:.3f} km/l")
   



def get_float_number():
    return float(input())


def get_number():
    return int(input())
 
main()    