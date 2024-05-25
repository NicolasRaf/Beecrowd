def main():
    #Entrada
    pontoA = input().split()
    pontoAX = float(pontoA[0])
    pontoAY = float(pontoA[1])
    
    pontoB = input().split()
    pontoBX = float(pontoB[0])
    pontoBY = float(pontoB[1])

    #Processamento
    distancia = raiz_quadrada(pontoAX,pontoAY,pontoBX,pontoBY)    

    #Saída
    print(f"{distancia:.4f}")


def raiz_quadrada(ax,ay,bx,by):
    return ((ax - bx)**2 + (ay - by)**2)**0.5


main()  