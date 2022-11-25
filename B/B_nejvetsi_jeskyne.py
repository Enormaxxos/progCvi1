import math
import sys

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
destroyedTiles = []
dots = []

def biggestCave(map):
    final = dict()

    dots = findAllPoints(map)
    # print(dots)

    def recursiveCave(map, pos):
        dots["notDone"].remove(pos)
        dots["done"].append(pos)
        dots["dict"][(pos[0],pos[1])] = "done"
        destroyedTiles.append(pos)

        possibleMoves = []

        for d in directions:
            try:
                newDot = dots["dict"][(pos[0]+d[0],pos[1]+d[1])]
            except KeyError:
                continue
            if newDot == "notDone":
                possibleMoves.append((pos[0]+d[0],pos[1]+d[1]))

        for posMove in possibleMoves:
            if dots["dict"][(posMove[0],posMove[1])] == "notDone":
                recursiveCave(map, posMove)

    while len(dots["notDone"]) > 0:
        recursiveCave(map, dots["notDone"][0])

        avgX, avgY = 0, 0
        for tile in destroyedTiles:
            avgX += tile[0]
            avgY += tile[1]
        avgX //= len(destroyedTiles)
        avgY //= len(destroyedTiles)

        final[len(destroyedTiles)] = (avgX, avgY)

        destroyedTiles.clear()

    returning = max(final)

    return returning, final[returning][0], final[returning][1]


def findAllPoints(map):
    ptsList = dict()
    ptsList["notDone"] = []
    ptsList["done"] = []
    ptsList["dict"] = dict()

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ".":
                ptsList["notDone"].append((i, j))
                ptsList["dict"][(i,j)] = "notDone"

    return ptsList


def inputHandler():
    final = []

    for line in sys.stdin:
        final.append(line.strip())

    return biggestCave(final)


print(*inputHandler())

# ....###.##.###
# ..##....##..##
# .##..##....###
# .#..##.....###
# .#######..####
# .##..###.##..#
# ###..#####...#

# .###..
# ...#..
# ##.###
# .#....
# ..####
# .#....

