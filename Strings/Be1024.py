## Criptografia ##

def main():
    #Entrada
    rodadas = int(input())

    #Processamento
    for i in range(rodadas):
        mensagem = input()
        textoDeslocado = deslocarLetras(mensagem)
        textoInvertido = inverterTexto(textoDeslocado)
        textoFinal = deslocarMetade(textoInvertido)

        #Saída
        print(textoFinal)
    

## Desloca todas a letras 3 posições a direita na tabela ASCII
def deslocarLetras(texto: str):

    novaFrase = ""

    for caractere in texto:
        codigoAtual = ord(caractere)
        
        if codigoAtual >= 65 and codigoAtual <= 90 or codigoAtual >= 97 and codigoAtual <= 122:
            novoCod = codigoAtual + 3
            novaFrase += chr(novoCod)
        else:
            novaFrase += caractere

    return(novaFrase)

## Inverte o texto recebido
def inverterTexto(texto: str):
    return texto[-1::-1]


## Desloca somente metade da frase uma posição a esquerda
def deslocarMetade(texto: str):
    tamanhoMetade = get_floor(len(texto)/2)
    novoTexto = texto[0:tamanhoMetade]

    for caractere in texto[tamanhoMetade:]:
        codigoAtual = ord(caractere)
        novoCod = codigoAtual - 1
        novoTexto += chr(novoCod)
    
    return novoTexto

## Faz a função do "math.floor"
def get_floor(num):

    if num == int(num):
        return int(num)
    
    if num > 0:
        return int(num)
    else:
        return int(num) - 1

main()      