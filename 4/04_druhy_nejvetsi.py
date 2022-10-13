a = input().split(" ")

uniqueSet = set()
arr = []

for i in range(len(a)):
    if a[i] == '-1':
        break
    uniqueSet.add(int(a[i]))

for uniqueNum in uniqueSet:
    arr.append(uniqueNum)

arr.sort()

print(arr[-2])