#heapSort

class BinaryHeap:
    
    def __init__(self):
        self.heap = []

    def add(self,val): # parent [(i-1) // 2]
        self.heap.append(val)
        index = len(self.heap) - 1

        correct = False

        while not correct:
            correct = True
            hasParent = (index-1)//2 >= 0
            if hasParent and self.heap[(index-1)//2] > val:
                # print(f'switched self.heap[(index-1)//2] = {self.heap[(index-1)//2]} and self.heap[index] = {self.heap[index]}')
                self.heap[(index-1)//2],self.heap[index] = self.heap[index],self.heap[(index-1)//2]
                index = (index-1)//2
                correct = False

        return True

    def removeMin(self):  # children [2*i + 1] a [2*i + 2]
        returning = self.heap[0]
        if len(self.heap) == 1:
            return returning

        self.heap[0] = self.heap.pop()

        index = 0

        correct = False

        while not correct:
            correct = True
            childOne = self.heap[2*index + 1] if (2*index + 1 < len(self.heap)) else None # find both children
            childTwo = self.heap[2*index + 2] if (2*index + 2 < len(self.heap)) else None

            smallerChildVal = None
            indexOfSmallerChild = None

            if childOne == None and childTwo == None: # has no children
                continue

            elif childOne != None and childTwo == None: # has only childOne (having only childTwo is not possible)
                smallerChildVal = childOne
                indexOfSmallerChild = 2*index + 1

            else: # has both children, check which one is smaller
                smallerChildVal = min(childOne,childTwo)
                indexOfSmallerChild = (2*index+1) if smallerChildVal == childOne else 2*index+2

            if self.heap[index] > smallerChildVal: # if parent is bigger than its smaller child, switch them
                self.heap[index],self.heap[indexOfSmallerChild] = self.heap[indexOfSmallerChild],self.heap[index]
                index = indexOfSmallerChild
                correct = False


        return returning


def heapSort(numList):

    heap = BinaryHeap() # create binary heap

    finalList = []

    for i in range(len(numList)): # insert all numbers via heap.add function
        heap.add(numList[i])

    # print(heap.heap)

    for i in range(len(numList)): # get smallest number from heap, insert to finalList, remove from heap, correct the heap
        finalList.append(heap.removeMin())

    return finalList

def inputHandler(inputString):
    strList = inputString.split(" ")
    return heapSort([int(x) for x in strList])

final = inputHandler(input())
print(*final)