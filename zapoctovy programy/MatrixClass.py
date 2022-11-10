from fractions import Fraction
from math import floor,ceil

# TODO:
#     -rank
#     -REF tvar
#     -inverse
#     -homogeneous solutions..?
#     -non-homogeneous solutions..? (requires Vector class / 1 x self._m matrix)

class Matrix:

    def __init__(self,data):
        self.matrix = []
        self._m = len(data)
        self._n = len(data[0])
        self.transposed = False

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

        for i in range(self._m):
            row = "| "
            for j in range(self._n):
                row += centerText(str(self.matrix[i][j]), allUnitCharCount) + " "

            if i == 0 and self.transposed:
                final += row[:-1] + f" |T\n"
            else:
                final += row[:-1] + f" |\n"
            

        return final[:-1]

    def __getitem__(self,indexTuple):# MATRIX[i,j] - tuple indexing
        i,j = indexTuple
        return self.matrix[i-1][j-1]

    # ----MATH OPERATIONS----

    def _add(self,other,self_assign=False):
        if type(other) != Matrix:
            raise Exception("You can only add another matrix to this matrix.")
        if self._n != other._n or self._m != other._m:
            raise Exception("Matrix addition is only defined for two matrices of the same size.")

        if self_assign:
            for row in range(self._m):
                for col in range(self._n):
                    self.matrix[row][col] += other.matrix[row][col]
            return True
        else:
            final = []
            for row in range(self._m):
                final.append([])

                for col in range(self._n):
                    final.append(self.matrix[row][col] + other.matrix[row][col])
            return final

    def __add__(self,other): # MATRIX+MATRIX
        return self._add(other)

    def _constantMult(self,val):
        newMatrix = []

        for i in range(len(self.matrix)):
            newMatrix.append(self.matrix[i][:])
            for j in range(len(newMatrix[i])):
                newMatrix[i][j] *= val

        return Matrix(newMatrix)

    def _matrixMult(self,other):

        final = []

        if self._n != other._m:
            raise Exception("Left matrices' column count doesn't equal right matrices' row count. Matrix multiplication is not defined")
        
        for i in range(self._m):
            final.append([])
            for j in range(other._n):
                final[i].append(0)
                for k in range(self._n):
                    final[i][j] += self.matrix[i][k] * other.matrix[k][j]
        
        return Matrix(final)

    def __mul__(self,val): # n*MATRIX / MATRIX*MATRIX
        if type(val) == int or type(val) == float:
            return self._constantMult(Fraction(val).limit_denominator())
        if type(val) == Matrix:
            return self._matrixMult(val)

    def _transposed(self):

        newMatrixList = []
        self.newN = self._m
        self.newM = self._n

        for i in range(self.newM):
            newMatrixList.append([])
            for j in range(self.newN):
                newMatrixList[i].append(self.matrix[j][i])

        newMatrix = Matrix(newMatrixList)
        newMatrix.transposed = not self.transposed

        return newMatrix

    def __invert__(self): # tilde(~)MATRIX - calls _transposed - Transposes Matrix
        return self._transposed()

    # ----CONSTRUCTORS----

    @staticmethod
    def fromString(matrixString,rowSplitChar="@",colSplitChar="&"): # DEFAULTS - rowSplitChar = "@" colSplitChar = "&"

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

    def fromInput(): # unlike other constructors requires user input
        print("Use ampersand (&) as a unit separator between columns. \nWhen you finish inputting row, hit ENTER. \nWhen you finish inputting matrix, leave row empty and hit ENTER.")
        colSeparator = '&'

        finalList = []

        row = input()
        rowSplit = row.split(colSeparator)
        n = len(rowSplit)
        finalList.append([Fraction(unit) for unit in rowSplit])

        while row != "":
            row = input()
            rowSplit = row.split(colSeparator)

            if row == "":
                break

            if len(rowSplit) != n:
                raise Exception("All rows must have the same number of units.")
            
            finalList.append([Fraction(unit) for unit in rowSplit])

        return Matrix(finalList)



# a = Matrix.fromLists([16/3,50],[40,48])
# b = Matrix.from2DList([[4,5],[3,5]])

# input("_____________")

# print("a.toString()",a.toString())
# print("b.toString()",b.toString())


# input("_____________")

# i = int(input("i="))
# j = int(input("j="))

# print(f"a[{i},{j}]", a[i,j])
