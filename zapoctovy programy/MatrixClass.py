from fractions import Fraction
from math import floor

class Matrix:

    def __init__(self,data):
        self.matrix = []
        self.m = len(data)
        self.n = len(data[0])

        for i in range(len(data)):
            self.matrix.append([])
            self.matrix[i] = data[i][:]

    def toString(self):
        return self.matrix

    def add(self,other):
        if type(other) != Matrix:
            raise Exception("You can only add another matrix to this matrix.")
        


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
                raise Exception("All rows must have the same number of units.")

            for j in range(len(units)):
                fraction = Fraction(units[j])
                if abs(float(fraction) - round(float(fraction))) < tolerance:
                    finalList[i].append(round(fraction))
                else:
                    finalList[i].append(fraction)

        return Matrix(finalList)

    def fromLists(*matrixLists):
        finalList = []
        n = len(matrixLists[0])

        for lst in matrixLists:
            appendingList = []
            if len(lst) != n:
                raise Exception("All rows must have the same number of units.")

            for unit in lst:
                appendingList.append(Fraction(str(unit)).limit_denominator())

            finalList.append(appendingList)

        return Matrix(finalList)

    def from2DList(matrixList):
        finalList = []
        n = len(matrixList[0])

        for row in matrixList:
            
            if len(row) != n:
                raise Exception("All rows must have the same number of units.")

            finalList.append([Fraction(str(unit)).limit_denominator() for unit in row])

        return Matrix(finalList)


    