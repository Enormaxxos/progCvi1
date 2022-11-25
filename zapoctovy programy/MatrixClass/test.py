a = [[1,2,3],[4,5,6],[7,8,9]]

aCopy = []
for row in a:
    aCopy.append(row[:])

a[1][2] = 777
print(a)
print(aCopy)