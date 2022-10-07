from math import inf

inputStr = input()
inputArr = inputStr.split(" ")

final = []
for i in range(7):
    final.append(0)

lastIndex = -1

for i in range(len(inputArr)-1,-1,-1):
    try:
        inputArr[i] = int(inputArr[i])
    except ValueError:
        inputArr.pop(i)

for i in range(len(inputArr)):
    if inputArr[i] % 2 == 1:
        final[0] = inputArr[i]
        inputArr = inputArr[0:i]
        break

final[1] = min(inputArr)
final[2] = max(inputArr)

for i in range(len(inputArr)):
    if inputArr[i] > 0 and inputArr[i] <=5:
        final[3]+=1
    elif inputArr[i] > 5 and inputArr[i] <=10:
        final[4] +=1
    elif inputArr[i] > 10 and inputArr[i] <=15:
        final[5] +=1
    elif inputArr[i] > 15 and inputArr[i] <=20:
        final[6] +=1
    
print(f"{final[0]}\n{final[1]}\n{final[2]}\n{final[3]}\n{final[4]}\n{final[5]}\n{final[6]}\n")
