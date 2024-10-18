
def main():
    #Entrada
    nota1 = get_number() 
    nota2 = get_number() 
    nota3 = get_number() 
    
    #Processamento
    media = ((nota1* 2) + (nota2* 3) + (nota3 * 5))/10 

    #Saida
    print(f"MEDIA = {media:.1f}")
  

def get_number():
    return float(input())

    
main()
