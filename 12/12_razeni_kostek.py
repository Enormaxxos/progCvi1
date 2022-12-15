sortedBricks = []
import sys

def findLongest(tiles,tileCount,startingNum):

    # initialize tilesDict ( tilesDict[i] = [Brick(i,a),Brick(i,b),...] )
    tilesDict = dict()
    for brick in tiles:
        try:
            tilesDict[brick[0]].append(brick)
        except KeyError:
            tilesDict[brick[0]] = []
            tilesDict[brick[0]].append(brick)

        try:
            tilesDict[brick[1]].append(brick[::-1])
        except KeyError:
            tilesDict[brick[1]] = []
            tilesDict[brick[1]].append(brick[::-1])

    def findLongestRecursive(currList,tiles,nextNum):
        global sortedBricks

        if len(tiles[nextNum]) == 0:
            sortedBricks.append(currList)
            return

        for brick in tiles[nextNum]:
            currListCopy = currList.copy()
            currListCopy.append(brick)

            temp = tiles.copy()
            for key in temp.keys():
                temp[key] = temp[key][:]

            temp[brick[0]].remove(brick)
            temp[brick[1]].remove(brick[::-1])
            findLongestRecursive(currListCopy,temp,brick[1])

    findLongestRecursive([],tilesDict,startingNum)

def inputHandler():
    # tileCount, startingNum = input().split()
    # tiles = input().split()
    tileCount,startingNum = sys.stdin.readline().strip().split()
    tiles = sys.stdin.readline().strip().split()


    findLongest(tiles,int(tileCount),startingNum)

    final = ""

    longestDomino = max(sortedBricks,key= lambda lst: len(lst))

    final = str(len(longestDomino)) + "\n"

    for unit in longestDomino:
        final += unit + " "

    return final


print(inputHandler())