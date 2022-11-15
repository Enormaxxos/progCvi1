# FIXME: 
# rowSum and zeroReplacement not global, tests() cant access

def magicMatrix(matrix):
    m = len(matrix)

    rowSum = None
    zeroReplacement = None

    def tests(numList):
        if 0 not in numList and rowSum == None:
            rowSum = sum(numList)
        elif 0 not in numList and rowSum != None and sum(numList) != rowSum:
            return False
        elif 0 in numList and rowSum != None and zeroReplacement != None and (sum(numList) + zeroReplacement != rowSum):
            return False
        elif 0 in numList and rowSum != None and zeroReplacement == None:
            zeroReplacement = rowSum - sum(numList)

    def checkCol(j):
        col = [matrix[i][j] for i in range(m)]

        tests(col)

    def checkRow(i):
        row = [matrix[i][j] for i in range(m)]

        tests(row)

    def checkMainDiag():
        diag = [matrix[i][i] for i in range(m)]

        tests(diag)

    def checkOtherDiag():
        diag = [matrix[i][m-i-1] for i in range(m)]

    for i in range(m):
        if checkCol(i) == False or checkRow(i) == False:
            return "Can't be magic"

    if checkMainDiag() == False or checkOtherDiag() == False:
        return "Can't be magic"

    final = ""
    for row in matrix:
        stringLine = ""
        for unit in row:
            stringLine += str(unit) + " "
        final += stringLine[:-1] + "\n"
    return final[:-1]


def inputHandler():
    stringInput = ""
    inputLine = input()
    rowCount = len(inputLine.split(" "))

    for i in range(rowCount-1):
        stringInput += input() + "\n"

    stringInput = stringInput[:-1]

    final = []
    inputRows = stringInput.split("\n")
    for row in inputRows:
        rowSplit = row.split(" ")
        final.append([int(unit) for unit in rowSplit])

    return magicMatrix(final)

inputHandler()
