def listIntersection(list1,list2):
    set1 = set()
    set2 = set()

    for item in list1:
        set1.add(int(item))

    for item in list2:
        set2.add(int(item))

    intersection = set1.intersection(set2)

    finalString = ""

    for item in sorted(intersection):
        finalString += f"{item} "

    return finalString[:-1]

inputString = input()
inputList = inputString.split()
splitIndex = inputList.index("-1")
listOne = inputList[0:splitIndex]
listTwo = inputList[splitIndex+1:len(inputList)]

print(listIntersection(listOne,listTwo))