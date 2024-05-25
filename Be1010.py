def main():
    #Entrada
    
    item = input().split(" ")
    cod = int(item[0])
    qt = int(item[1])
    valor = float(item[2])
    
    item2 = input().split(" ")
    cod2 = int(item2[0])
    qt2 = int(item2[1])
    valor2 = float(item2[2])
    

    #Processamento
    total = (qt * valor) + (qt2 * valor2)

    #Saída
    print(f"VALOR A PAGAR: R$ {total:.2f}")




main()