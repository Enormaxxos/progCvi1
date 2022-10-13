a = int(input())

goodNumbers = []

for number in range(1,a+1):
    numStr = str(number)
    goodNum = True
    for i in range(len(numStr)):
        if numStr[i] == '0':
            goodNum = False
            continue
        if number % int(numStr[i]) != 0:
            goodNum = False
    
    if goodNum:
        goodNumbers.append(number)

print(len(goodNumbers))
