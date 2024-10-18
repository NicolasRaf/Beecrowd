
def main():
    #Entrada
    nota1 = get_number() 
    nota2 = get_number() 
    
    #Processamento
    media = ((nota1* 3.5) + (nota2* 7.5))/11

    #Saida
    print(f"MEDIA = {media:.5f}")
  

def get_number():
    return float(input())

    
main()
