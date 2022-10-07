from random import randrange
from tkinter import Canvas
from math import *

canvasWidth,canvasHeight = 800,800
outlineWidth = 3 

main = Canvas(width=canvasWidth,height=canvasHeight,bg="white")
main.pack()

possibleSteps = []

## SQUARE CLASS ##

class Square:
    def __init__(self,x,y,w,i,j):
        self.x,self.y,self.w,self.i,self.j = x,y,w,i,j
        self.done = False

        self.sides = [True,True,True,True] #N,E,S,W

    def checkNeighbors(self):
        neighbors = []

        if self.i+1 < sqC and sqArr[self.i+1][self.j].done == False:
            neighbors.append(sqArr[self.i+1][self.j])
        if self.i-1 >= 0 and sqArr[self.i-1][self.j].done == False:
            neighbors.append(sqArr[self.i-1][self.j])
        if self.j+1 < sqC and sqArr[self.i][self.j+1].done == False:
            neighbors.append(sqArr[self.i][self.j+1])
        if self.j-1 >= 0 and sqArr[self.i][self.j-1].done == False:
            neighbors.append(sqArr[self.i][self.j-1])

        return neighbors

    def show(self):
        if not self.done:
            main.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.w,fill="white",outline="white")
        elif self.i == sqC-1 and self.j ==sqC-1:
            main.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.w,fill="blue",outline="blue")
        else:
            main.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.w,fill="red",outline="red")

        if self.sides[0] == True:
            main.create_line(self.x,self.y,self.x+self.w,self.y,fill="black",width=outlineWidth)
        if self.sides[1] == True:
            main.create_line(self.x+self.w,self.y,self.x+self.w,self.y+self.w,fill="black",width=outlineWidth)
        if self.sides[2] == True:
            main.create_line(self.x+self.w,self.y+self.w,self.x,self.y+self.w,fill="black",width=outlineWidth)
        if self.sides[3] == True:
            main.create_line(self.x,self.y+self.w,self.x,self.y,fill="black",width=outlineWidth)


def removeWalls(sqA,sqB):
    possibleSteps.append((sqA.i,sqA.j,sqB.i,sqB.j))

    if sqA.i-sqB.i == 1:
        sqA.sides[3] = False
        sqB.sides[1] = False
    if sqA.i-sqB.i == -1:
        sqA.sides[1] = False
        sqB.sides[3] = False
    if sqA.j-sqB.j == 1:
        sqA.sides[0] = False
        sqB.sides[2] = False
    if sqA.j-sqB.j == -1:
        sqA.sides[2] = False
        sqB.sides[0] = False


## SQUARE CLASS ##

sqC = 12
sqW = canvasWidth // sqC

sqArr = []


currX,currY = 0,0

def setup():
    for i in range(sqC):
        sqArr.append([])
        for j in range(sqC):
            sqArr[i].append(Square(i*sqW,j*sqW,sqW,i,j))
    

def draw(currI,currJ):
    for i in range(sqC):
        for j in range(sqC):
            sqArr[i][j].show()

    #____POSSIBLE STEPS VIS____
    # for i in range(len(possibleSteps)): 
    #     sqA = sqArr[possibleSteps[i][0]][possibleSteps[i][1]]
    #     sqB = sqArr[possibleSteps[i][2]][possibleSteps[i][3]]
    #     main.create_line(sqA.x+sqW/2,sqA.y+sqW/2,sqB.x+sqW/2,sqB.y+sqW/2,fill="black",width=3)

    main.create_rectangle(currI*sqW,currJ*sqW,(currI+1)*sqW,(currJ+1)*sqW,fill="blue")

def drawPath(path):
    for i in range(len(path)): 
        sqA = sqArr[path[i][0]][path[i][1]]
        sqB = sqArr[path[i][2]][path[i][3]]
        main.create_line(sqA.x+sqW/2,sqA.y+sqW/2,sqB.x+sqW/2,sqB.y+sqW/2,fill="green",width=3)
    
def vykresli(sq):
    main.after(16,main.delete('all'))
    draw(sq.i,sq.j)
    main.update()

def vykresliCestu(path):   
    main.after(16,main.delete('all'))
    draw(0,0)
    drawPath(path)
    main.update()

def mazeGen(sq):
    sq.done = True
    neighbors = sq.checkNeighbors()
    if len(neighbors) == 0:
        vykresli(sq)
        return
        
    else:
        while len(neighbors) > 0:         
            neighbors = sq.checkNeighbors()
            if len(neighbors) == 0:
                vykresli(sq)
                return
            vykresli(sq)
            nextIndex = randrange(0,len(neighbors))
            next = neighbors.pop(nextIndex)
            removeWalls(sq,next)
            mazeGen(next)
        vykresli(sq)
        return

def solve(pos,path):

    vykresliCestu(path)

    if pos[0] == len(sqArr)-1 and pos[1] == len(sqArr)-1:
        return path

    possibleMoves = []

    for i in range(len(possibleSteps)):
        if possibleSteps[i][0] == pos[0] and possibleSteps[i][1] == pos[1]:
            possibleMoves.append(possibleSteps[i])

    possibleMoves.reverse()

    for i in range(len(possibleMoves)-1,-1,-1):
        vykresliCestu(path)
        a = solve((possibleMoves[i][2],possibleMoves[i][3]),path + [possibleMoves[i]])
        if type(a) == type([]):
            return a
        possibleMoves.pop()
        
    vykresliCestu(path)
    return False
            

            

setup()
mazeGen(sqArr[0][0])

print(solve((0,0),[]))

input()
