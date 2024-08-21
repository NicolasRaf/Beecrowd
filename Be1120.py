def main():
    brokenNum = ""
    allNumber = ""
    result = ""

    while True:
        
        # Entrada
        contract = input().split(" ")
        brokenNum = contract[0]
        allNumber = contract[1]

        # Processamento
        for num in allNumber:
            if num != brokenNum:
                result += num
                
        if brokenNum == "0" and allNumber == "0":
            break

        # Saída
        if result == "":
            print(0)
        else:
            print(int(result))
        
        result = ""
main()