pocet = int(input())

def josef(arr):
    index = 1
    shouldStartOnIndexOne = len(arr) % 2 == 0

    while len(arr) > 1:
        try:
            arr.pop(index)
            index = (index + 1)
        except IndexError:
            index = 1 if shouldStartOnIndexOne else 0
            if len(arr) % 2 == 1:
                shouldStartOnIndexOne = not shouldStartOnIndexOne

    return arr[0]

if pocet < 1:
    print("ERROR")
else:
    print(josef(list(range(pocet)))+1)