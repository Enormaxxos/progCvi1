#countingSort

def countingSort(numList):
    counts = []
    final = []
    #najdi nejvetsi cislo a vytvor nulove pole s delkou tohoto cisla,
    for i in range(max(numList)+1):
        counts.append(0)

    #projdi vsechny cisla, pro kazde cislo A pricti jednicku v counts[A]
    for num in numList:
        counts[num] += 1

    #projdi cely seznam counts, pro counts[i] != 0 vloz do final hodnotu i
    for i in range(len(counts)):
        while counts[i] > 0:
            final.append(i)
            counts[i] -= 1
    
    return final

def inputHandler(inputString):
    strList = inputString.split(" ")
    return countingSort([int(x) for x in strList])

final = inputHandler(input())
print(*final)
