## LED ##

def ledsCount(number):
    ledsNumber = [6,2,5,5,4,5,6,3,7,6] # Array em que o valor refere-se aos leds usados no indice(0 -> 6 leds) 
    ledsSum: int = 0

    for digit in number:
        ledsSum += ledsNumber[int(digit)]

    return ledsSum


def main():
    ## Entrada
    cases: int = int(input()) 

    for _ in range(cases):
        ## Processamento
        number: str = input()
        ledsAmount: int = ledsCount(number)

        ## Saída
        print(ledsAmount,"leds")

main()