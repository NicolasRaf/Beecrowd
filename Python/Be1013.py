def main():
    #Entrada
    valores= input().split(" ")
    valorA = int(valores[0])
    valorB = int(valores[1])
    valorC = int(valores[2])

    #Processamento
    maiorAB =   (valorA + valorB + abs(valorA - valorB))/2
    valor_maior = int((maiorAB + valorC + abs(maiorAB - valorC))/2)


    #Saída
    print(f"{valor_maior} eh o maior")
   

main() 