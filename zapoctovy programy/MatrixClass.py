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

    def directory(self):
        print(dir(self))

    def toString(self,name=""):
        final = f"\n-- Matrix '{name}'--\n"

        for i in range(self.m):
            row = ""
            for j in range(self.n):
                unit = self.matrix[i][j]
                row += str(unit.numerator) if (unit.denominator == 1) else f"{unit.numerator}/{unit.denominator}"
                row += " "

            final += row[:-1] + "\n"

        return final[:-1]

    # ----MATH OPERATIONS----

    def add(self,other,self_assign=True):
        if type(other) != Matrix:
            raise Exception("You can only add another matrix to this matrix.")
        if self.n != other.n or self.m != other.m:
            raise Exception("Matrix addition is only defined for two matrices of the same size.")

        if self_assign:
            for row in range(self.m):
                for col in range(self.n):
                    self.matrix[row][col] += other.matrix[row][col]
            return True
        else:
            final = []
            for row in range(self.m):
                final.append([])

                for col in range(self.n):
                    final.append(self.matrix[row][col] + other.matrix[row][col])
            return final

    # ----CONSTRUCTORS----
    @staticmethod
    def fromString(matrixString,rowSplitChar="@",colSplitChar="&"): # rowSplitChar = "@" colSplitChar = "&"

        finalList = []
    
        rows = matrixString.split(rowSplitChar)
        n = len(rows[0].split(colSplitChar))

        for i in range(len(rows)):
            units = rows[i].split(colSplitChar)

            if len(units) != n:
                raise Exception("All rows must have the same number of units.")

            finalList.append([Fraction(str(unit)).limit_denominator() for unit in units])

        return Matrix(finalList)

    def fromLists(*matrixLists):
        finalList = []
        n = len(matrixLists[0])

        for lst in matrixLists:
            if len(lst) != n:
                raise Exception("All rows must have the same number of units.")

            finalList.append([Fraction(str(unit)).limit_denominator() for unit in lst])

        return Matrix(finalList)

    def from2DList(matrixList):
        finalList = []
        n = len(matrixList[0])

        for row in matrixList:
            
            if len(row) != n:
                raise Exception("All rows must have the same number of units.")

            finalList.append([Fraction(str(unit)).limit_denominator() for unit in row])

        return Matrix(finalList)

a = Matrix.fromString("2&3&4/5@4&9/4&3@3&4&5")
b = Matrix.fromLists([2/3,4,5],[3,5,6])
c = Matrix.from2DList([[2/3,4,5],[3,5,6]])

print(a.toString("a"))
print(b.toString("b"))
print(c.toString())

input("...")
print(f"b before = {b.toString()}")

print(b.add(c))

print(f"b after = {b.toString()}")

input("...")

a.directory()
