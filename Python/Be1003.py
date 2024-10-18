
def main():
    
    #Entrada
    num1 = get_number()
    num2 = get_number()
    
    #Processamento
    resultado = num1 + num2
    
    #Saída
    print(f"SOMA = {resultado}")
    
def get_number():
    return int(input())
    
main()