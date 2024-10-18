def main():
    #Entrada
    raio = get_float_number()
    pi =  3.14159

    #Processamento
    volume = (4.0/3) * pi * raio**3

    #Saída
    print(f"VOLUME = {volume:.3f}")


def get_float_number():
    return float(input())


def get_number():
    return int(input())

main() 