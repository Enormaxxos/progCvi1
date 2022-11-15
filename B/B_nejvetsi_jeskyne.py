import math

directions = [(1,0),(0,1),(-1,0),(0,-1)]
mapS = 0
destroyedTiles = []
dots = []

def biggestCave(map):
    final = dict()

    dots = findAllPoints(map)
    # print(dots)

    def recursiveCave(map,pos):
        dots["notDone"].remove(pos)
        dots["done"].append(pos)
        destroyedTiles.append(pos)

        possibleMoves = []

        for i in range(len(dots["notDone"])):
            if math.sqrt((dots["notDone"][i][0]-pos[0])**2 + (dots["notDone"][i][1]-pos[1])**2) == 1:
                possibleMoves.append(dots["notDone"][i])
        
        # print(f"On pos={pos}, possibleMoves are {possibleMoves}")

        for posMove in possibleMoves:
            if posMove not in dots["done"]:
                recursiveCave(map,posMove)

    while len(dots["notDone"]) > 0:
        recursiveCave(map,dots["notDone"][0])

        avgX,avgY = 0,0
        for tile in destroyedTiles:
            avgX += tile[0]
            avgY += tile[1]
        avgX //= len(destroyedTiles)
        avgY //= len(destroyedTiles)

        final[len(destroyedTiles)] = (avgX,avgY)

        destroyedTiles.clear()

    print(f"vsechny jeskyne = {final}")


    return max(final),final[max(final)][0],final[max(final)][1]
    
def findAllPoints(map):
    ptsList = dict()
    ptsList["notDone"] = []
    ptsList["done"] = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ".":
                ptsList["notDone"].append((i,j))

    return ptsList

def inputHandler():
    final = []
    line = input()

    mapS = len(line)
    mapR = 0

    while len(line) > 0:  
        final.append(line)
        mapR += 1
        line = input()

    # print("--MAP--")
    # print(final)
    # print("-------")
    # print(f"mapS={mapS}")
    # print(f"mapR={mapR}")

    return biggestCave(final)

printed = inputHandler()
printedString = ""

for unit in printed:
    printedString += str(unit) + " "

print(printedString[:-1])