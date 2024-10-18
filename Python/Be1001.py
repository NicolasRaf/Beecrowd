def main():
    
    #Entrada
    numero1 = get_number()
    numero2 = get_number()
    
    #Processamento
    soma = numero1 + numero2

    #Saida
    print(f"X = {soma}")
  

def get_number():
    return int(input())

    
main()