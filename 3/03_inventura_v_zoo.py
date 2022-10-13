a = input().split(" ")
num = int(a[0])
contentArr = a[1].split(";")

if num == 1:
    for i in range(len(contentArr)):
        print(f"V zoo je {contentArr[i]}, které má {len(contentArr[i])} písmen.")

elif num == 2:
    lionNum = 0

    for i in range(len(contentArr)):
        if contentArr[i].lower() == "lev":
            lionNum += 1
    print(lionNum)

elif num == 3:
    minLen = 100
    maxLen = 0
    for i in range(len(contentArr)):
        if len(contentArr[i]) > maxLen:
            maxLen = len(contentArr[i])
        if len(contentArr[i]) < minLen:
            minLen = len(contentArr[i])

    print(f"{len(contentArr)} {minLen} {maxLen}")

elif num == 4:
    count = 0
    for i in range(len(contentArr)):
        if contentArr[i].startswith("k") and contentArr[i].endswith(('a','e','i','o','u','y')):
            count += 1
    print(count)

elif num == 5:
    print(contentArr[-4])

elif num == 6:
    uniqueSet = set()
    for i in range(len(contentArr)):
        if contentArr[i].startswith('l'):
            uniqueSet.add(contentArr[i])
    print(*uniqueSet,sep=" ")

elif num == 7:
    uniqueSet = set()
    for i in range(len(contentArr)):
        uniqueSet.add(contentArr[i])
    
    sum = 0
    for zvire in uniqueSet:
        sum += len(zvire)

    print(sum)

elif num == 8:
    index = -1
    maxLen = 0
    for i in range(len(contentArr)):
        if len(contentArr[i]) > maxLen:
            index = i
            maxLen = len(contentArr[i])
    
    print(contentArr[index])

elif num == 9:
    for i in range(len(contentArr)-1):
        print(f"{contentArr[i]} je lepší než {contentArr[i+1]}.")

elif num == 10:
    for i in range(len(contentArr)-1):
        if len(contentArr[i]) > len(contentArr[i+1]):
            print(f'{contentArr[i]} je delší než {contentArr[i+1]}.')
        elif len(contentArr[i]) < len(contentArr[i+1]):
            print(f'{contentArr[i]} je kratší než {contentArr[i+1]}.')
        else:
            print(f'{contentArr[i]} je stejné jako {contentArr[i+1]}.')

elif num == 11:
    letters = []
    for i in range(12):
        letters.append(0)

    for i in range(len(contentArr)):
        for j in range(len(contentArr[i])):
            letterIndex = ord(contentArr[i][j])-ord("a")
            if letterIndex < 12:
                letters[letterIndex] += 1
    
    for i in range(len(letters)):
        print(f"Písmeno {chr(i+ord('A'))} je v seznamu zvířat {letters[i]}krát.")
