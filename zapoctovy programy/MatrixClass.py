from fractions import Fraction
from math import floor

class Matrix:

    def __init__(self,data):
        self.matrix = []

        for i in range(len(data)):
            self.matrix.append([])
            self.matrix[i] = data[i][:]

    def toString(self):
        return self.matrix

    @staticmethod
    def fromString(matrixString,rowSplitChar="@",colSplitChar="&"): # rowSplitChar = "@" colSplitChar = "&"

        tolerance = 0.0001

        finalList = []
    
        rows = matrixString.split(rowSplitChar)
        m = len(rows)

        for i in range(len(rows)):
            finalList.append([])
            units = rows[i].split(colSplitChar)
            if i == 0:
                n = len(units)
            elif len(units) != n:
                raise SyntaxError

            for j in range(len(units)):
                fraction = Fraction(units[j])
                if abs(float(fraction) - round(float(fraction))) < tolerance:
                    finalList[i].append(round(fraction))
                else:
                    finalList[i].append(fraction)

        return Matrix(finalList)

    def fromLists(*matrixLists):
        finalList = []
        for l in matrixLists:
            finalList.append(l)
            
        return Matrix(finalList)

    def from2DList(matrixList):
        return Matrix(matrixList)


a = Matrix.fromLists([2,3,4],[3,4,5],[4,5,6])
print(a.toString())



    