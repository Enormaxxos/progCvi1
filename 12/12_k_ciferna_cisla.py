#FIXME: nekde se to zasekne a nechce to pustit dal (edge case..?)

def genPerm(currPerm,currPermSum):
    global final

    if len(currPerm) == digitCount and currPermSum == digitSum:
        final += "".join([str(unit) for unit in currPerm]) + "\n"
        return

    if currPermSum > digitSum: # spatne
        return

    if len(currPerm) == digitCount and currPermSum != digitSum:
        return

    startIndex = 0 if len(currPerm) > 0 else 1
    for i in range(startIndex,10):
        temp = currPerm[:]
        temp.append(i)

        genPerm(temp,currPermSum+i)

if __name__ == "__main__":
    final = ""

    correctPerms = []
    digitCount,digitSum = [int(unit) for unit in input().split(" ")]

    if digitCount * 9 < digitSum:
        print()
    else:
        genPerm([],0)

        print(final[:-1])
