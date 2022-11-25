def hasTwoLineSegCommonPoint(A,B,C,D): # Line AB ?intersects? Line CD
    
    def pointTripletOrientation(a,b,c):
        det = (b[0]-a[0]) * (c[1]-b[1]) - (b[1]-a[1]) * (c[0]-b[0])
        print(det)

        if det == 0:
            return "arranged"
        elif det > 0:
            return "cw"
        elif det < 0:
            return "ccw"


def inputHandler(inputString):
    x1,y1,x2,y2,x3,y3,x4,y4 = inputString.split(" ")
    return hasTwoLineSegCommonPoint((x1,y1),(x2,y2),(x3,y3),(x4,y4))

print(inputHandler(input()))