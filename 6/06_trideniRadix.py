#radixSort
from math import log10,floor

def radixSort(numList):
    strList = [str(x) for x in numList]

    # maxNumDigits = kolik cislic ma nejvetsi cislo, aby 
    # ostatni cislum mohly byt pridany leading zeros, podle kterych se bude tridit
    maxNumDigits = floor(log10(max(numList))) + 1
    # print('maxNumDigits =',maxNumDigits)

    # prida ke kazdemu cislu takovy pocet leading zeros, aby se pocet znaku vsech cisel rovnal
    for i in range(len(strList)): 
        while len(strList[i]) < maxNumDigits:
            strList[i] = "0" + strList[i]

    for i in range(maxNumDigits):
        newDict = dict()
        #kazde cislo se prida do slovniku podle momentalniho klice(i-te cislice)
        for j in range(len(strList)):
            try:
                newDict[int(strList[j][maxNumDigits-i-1])].append(strList[j])
            except KeyError:
                newDict[int(strList[j][maxNumDigits-i-1])] = []
                newDict[int(strList[j][maxNumDigits-i-1])].append(strList[j])

        #pomoci bubbleSort(stabilniho trizeni) se seradi klice
        keys = list(newDict.keys())
        for i in range(len(keys)):
            for j in range(len(keys) - i - 1):
                if keys[j] >= keys[j+1]:
                    keys[j],keys[j+1] = keys[j+1],keys[j]

        #premaze se seznam cisel, aby se do nej mohla zacit vkladat cisla pretrizena podle i-teho klice
        strList.clear()
        
        for key in keys:
            for val in newDict[key]:
                strList.append(val)

        # v i-te iteraci bude seznam pretrizen podle poslednich i cislic

    #vrati se setrizeny seznam prekonvertovany zpatky na integery ze stringu s leading zeros
    return [int(x) for x in strList]

def inputHandler(inputString):
    strList = inputString.split(" ")
    return radixSort([int(x) for x in strList])

final = inputHandler(input())
print(*final)



    

    