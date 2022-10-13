a = input()
newNum = ""

for i in range(len(a)-1,-1,-1):
    newNum += a[i]

print(newNum)
