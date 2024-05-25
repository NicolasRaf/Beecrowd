def main():
    #Entrada
    nome_funcionário = input()
    salario = get_float_number()
    total_vendas = get_float_number()

    #Processamento
    comissão = total_vendas * 0.15
    salario_total = salario + comissão

    #Saída
    print(f"TOTAL = R$ {salario_total:.2f}")


def get_float_number():
    return float(input())


def get_number():
    return int(input())

main()