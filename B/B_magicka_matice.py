rowSum = None
zeroReplacement = None

def magicMatrix(matrix):
    m = len(matrix)

    def tests(numList):
        global rowSum
        global zeroReplacement

        if 0 not in numList and rowSum == None:
            # print("setting new rowSum")
            # print("---")
            rowSum = sum(numList)
        elif 0 not in numList and rowSum != None and sum(numList) != rowSum:
            # print("returning False (sum doesnt correspond)")
            # print("---")
            return False
        elif 0 in numList and rowSum != None and zeroReplacement != None and (sum(numList) + zeroReplacement != rowSum):
            # print("returning False(sum with zeroReplacement doesnt correspond)")
            # print("---")
            return False
        elif 0 in numList and rowSum != None and zeroReplacement == None:
            # print("setting new zeroReplacement")
            # print("---")
            zeroReplacement = rowSum - sum(numList)

    def checkCol(j):
        col = [matrix[i][j] for i in range(m)]
        # print("---")
        # print(f"checking col {col}")

        return tests(col)

    def checkRow(i):
        row = [matrix[i][j] for j in range(m)]
        # print("---")
        # print(f"checking row {row}")


        return tests(row)

    def checkMainDiag():
        diag = [matrix[i][i] for i in range(m)]
        # print("---")
        # print(f"checking diag {diag}")
        

        return tests(diag)

    def checkOtherDiag():
        diag = [matrix[i][m-i-1] for i in range(m)]
        # print("---")
        # print(f"checking other diag {diag}")

        return tests(diag)

    for i in range(m):
        if checkCol(i) == False or checkRow(i) == False:
            return "Can't be magic"

    if checkMainDiag() == False or checkOtherDiag() == False:
        return "Can't be magic"

    # print(f"matrix = {matrix}")
    # print(f"zeroReplacement = {zeroReplacement}")

    final = ""
    for row in matrix:
        stringLine = ""
        for unit in row:
            if unit == 0:
                unit = zeroReplacement
            stringLine += str(unit) + " "
        final += stringLine[:-1] + "\n"
    return final[:-1]


def inputHandler():
    stringInput = ""
    inputLine = " ".join(input().split())
    rowCount = len(inputLine.split(" "))
    stringInput += inputLine + "\n"

    for i in range(rowCount-1):
        stringInput += " ".join(input().split()) + "\n"

    stringInput = stringInput[:-1]

    final = []
    inputRows = stringInput.split("\n")
    for row in inputRows:
        rowSplit = row.split(" ")
        final.append([int(unit) for unit in rowSplit])

    return magicMatrix(final)

print(inputHandler())
