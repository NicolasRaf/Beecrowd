def main():
    #Entrada
    numero_funcionário = get_number()
    horas_trabalhadas = get_number()
    valor_hora = get_float_number()

    #Processamento
    salario = horas_trabalhadas * valor_hora

    #Saída
    print(f"NUMBER = {numero_funcionário}")
    print(f"SALARY = U$ {salario:.2f}")



def get_float_number():
    return float(input())

def get_number():
    return int(input())

main()