## Coluna na Matriz ##

def doReduce(vector, work, initialValue: int = 0):
    accumulated = initialValue

    for i in vector:
        accumulated = work(accumulated, i)

    return accumulated


def main():
    colum = int(input())
    operation =  input().upper()
    matrix = []
    vector = []

    for i in range(144):
        vector.append(float(input()))

        if (i + 1) % 12 == 0:
            matrix.append(vector)
            vector = []

    columNumbers = list()

    for lines in matrix:
        columNumbers.append(lines[colum])

    result = (doReduce(columNumbers, lambda a, c : a + c)) if operation == "S" else (doReduce(columNumbers,  lambda a, c : a + c)/len(columNumbers))
    print(f"{result:.1f}")

main()
