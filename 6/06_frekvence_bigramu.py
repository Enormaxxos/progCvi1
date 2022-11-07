def bigramCount(str):
    str = str.lower()

    bigramDict = dict()

    strArr = str.split()

    for str in strArr:
        for i in range(len(str) - 1):
            bigram = str[i : i + 2]

            if not bigram.isalpha():
                continue

            try:
                bigramDict[bigram] += 1
            except KeyError:
                bigramDict[bigram] = 1

    
    sizeDict = dict()
    for key,val in bigramDict.items():
        try:
            sizeDict[val].append(key)
        except:
            sizeDict[val] = []
            sizeDict[val].append(key)

    finalString = ""

    sortedSizeDict = sorted(sizeDict,reverse=True)

    for key in sortedSizeDict:
        sortedBigrams = sorted(sizeDict[key])
        for bigram in sortedBigrams:
            finalString += f"{bigram} {key}\n"

    return finalString[:-1]
    


print(bigramCount(input()))