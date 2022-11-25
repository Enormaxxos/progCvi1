# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line_segment

# Ja se vam fakt omlouvam, jestli to budete cist. Nevedel jsem, jak to udelat lepe.
import random

def lineSeg_lineSeg_intersection(x1,y1,x2,y2,x3,y3,x4,y4):

    tNumerator = (x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)
    uNumerator = (x1-x3)*(y1-y2) - (y1-y3)*(x1-x2)

    tuDenominator = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

    print(f"tNum={tNumerator}")
    print(f"uNum={uNumerator}")

    if tuDenominator == 0 and tNumerator == 0 and uNumerator == 0:
        # primky zadane useckou jsou totozne, zjisti, jestli se usecky aspon castecne prekryvaji

        abVector = (x2-x1,y2-y1)
        cdVector = (x4-x3,y4-y3)
        acVector = (x3-x1,y3-y1)
        adVector = (x4-x1,y4-y1)

        # 5 moznosti rozlozeni bodu na primce(A vzdy pred B, C vzdy pred D) -
        #   -ABCD(non-intersect) - ac,ad > ab (stejne smery)
        #   -ACBD(intersect) - a
        #   -ACDB(intersect)
        #   -CADB(intersect)
        #   -CDAB(non-intersect)


        if cdVector[0] == -abVector[0]:
            cdVector[0] *= -1
            cdVector[1] *= -1
        


        # if y1 == y2 and y2 == y3 and y3 == y4: # usecky jsou vodorovne
        #     pass
        # elif x1 == x2 and x2 == x3 and x3 == x4: # cary jsou svisle
        #     pass
        # else: # cary nejsou svisle ani vodorovne
        #     pass

        

    if tuDenominator == 0 and (tNumerator != 0 or uNumerator != 0):
        #usecky jsou paralelni, nemaji spolecny bod
        print("parallel")
        return "NE"
    if tuDenominator != 0:
        #usecky jsou ruznobezne, muzou mit spolecny bod, checkni, jestli opravdu maji
        print("different direction")
        t = tNumerator / tuDenominator
        u = uNumerator / tuDenominator

        if t >= 0 and t <= 1 and u >= 0 and u <= 1:
            return ("ANO")
        else:
            return ("NE")


def inputHandler(inputString):
    coordList = inputString.split(" ")
    coordList = [int(x) for x in coordList]
    return lineSeg_lineSeg_intersection(*coordList)

print(inputHandler(input()))