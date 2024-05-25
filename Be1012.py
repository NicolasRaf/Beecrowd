def main():
    #Entrada
    pontos= input().split(" ")
    pontoA = float(pontos[0])
    pontoB = float(pontos[1])
    pontoC = float(pontos[2])
    pi = 3.14159

    #Processamento
    area_tri = (pontoA * pontoC)/2
    area_circ = pi * pontoC**2
    area_trap = ((pontoA + pontoB) * pontoC)/2
    area_quad = pontoB**2
    area_retan = pontoA * pontoB


    #Saída
    print(f"TRIANGULO: {area_tri:.3f}")
    print(f"CIRCULO: {area_circ:.3f}")
    print(f"TRAPEZIO: {area_trap:.3f}")
    print(f"QUADRADO: {area_quad:.3f}")
    print(f"RETANGULO: {area_retan:.3f}")
          


def get_float_number():
    return float(input())


def get_number():
    return int(input())

main() 