## Construindo Casas ##
import math

def calculateSide(houseSize,percent):
    return int(math.sqrt(houseSize/ (percent/100)))
    

def main():
    ## Entrada
    length, width, percent = map(int, input().split())  
    
    while length != 0:

        ## Processamento 
        houseSize = length * width
        terrainSide = calculateSide(houseSize,percent)

        ## Saída
        print(terrainSide)  
    
        try:
            length, width, percent = map(int, input().split())
        except:
            length = 0
main()