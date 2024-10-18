# -*- coding: utf-8 -*-

def main():
    #Entrada
    numero1 = get_number() 
    numero2 = get_number() 
    numero3 = get_number() 
    numero4 = get_number()
    
    #Processamento
    subtracao = ((numero1 * numero2) - (numero3 * numero4))

    #Saida
    print(f"DIFERENCA = {subtracao}")
  

def get_number():
    return int(input())

main()