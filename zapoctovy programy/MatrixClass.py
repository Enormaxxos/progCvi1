from fractions import Fraction
from math import floor,ceil

class Matrix:

    def __init__(self,data):
        self.matrix = []
        self.m = len(data)
        self.n = len(data[0])

        for i in range(len(data)):
            self.matrix.append([])
            self.matrix[i] = data[i][:]
   
    def toString(self):

        def centerText(text,charCount):
            textLen = len(text)
            beforeSpacesCount = floor((charCount - textLen)/2)
            afterSpacesCount = ceil((charCount - textLen)/2)
            return beforeSpacesCount * " " + text + afterSpacesCount * " "

        final = f"\n-- Matrix --\n"

        flatMatrix = [str(unit) for row in self.matrix for unit in row]
        allUnitCharCount = len(max(flatMatrix,key=len))

        for i in range(self.m):
            row = "| "
            for j in range(self.n):
                row += centerText(str(self.matrix[i][j]), allUnitCharCount) + " "

            final += row[:-1] + " |\n"

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

    def __add__(self,other):
        return self.add(other)

    def _constantMult(self,val):
        newMatrix = []

        for i in range(len(self.matrix)):
            newMatrix.append(self.matrix[i][:])
            for j in range(len(newMatrix[i])):
                newMatrix[i][j] *= val

        return Matrix(newMatrix)

    def _matrixMult(self,other):

        final = []

        if self.n != other.m:
            raise Exception("Left matrices' column count doesn't equal right matrices' row count. Matrix multiplication is not defined")
        
        for i in range(self.m):
            final.append([])
            for j in range(other.n):
                final[i].append(0)
                for k in range(self.n):
                    final[i][j] += self.matrix[i][k] * other.matrix[k][j]
        
        return Matrix(final)

    def __mul__(self,val):
        if type(val) == int:
            return self._constantMult(val)
        if type(val) == Matrix:
            print(f"others[1][1]=", val.matrix[0][0])
            return self._matrixMult(val)

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

a = Matrix.fromLists([16/3,40],[40,48])
b = Matrix.from2DList([[4,5],[3,5]])

input("_____________")

print("a.toString()",a.toString())
print("b.toString()",b.toString())


input("_____________")

print("(a*b).toString()",(a*b).toString())
print("(b*a).toString()",(b*a).toString())
