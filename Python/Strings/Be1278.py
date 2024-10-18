## Justificador ##

def spaceSentences(phrase):
    return phrase[0] + " " + phrase[1]

def main():
    ## Entrada
    cases: int = int(input())
    text = []

    ## Processamento
    for _ in range(cases):
        phrase = input().split() 
        text.append(spaceSentences(phrase))



    print(text)

main()