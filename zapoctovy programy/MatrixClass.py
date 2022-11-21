import os
from fractions import Fraction
from math import ceil, floor

# TODO:
#     -fromString constructor (&,@) - DONE
#     -from2darray constructor - DONE
#     -fromArrays constructor - DONE
#     -fromInput interactive constructor - DONE
#     -toString() pretty-print - DONE   
#     -matrix + matrix (addition) - DONE (plus sign)
#     -matrix * n (constant multiplication) - DONE (asterisk sign)
#     -matrix * matrix (matrix multiplication) - DONE (asterisk sign)
#     -transposition - DONE (tilde sign, unar)
#     -REF tvar - DONE
#     -rank - DONE
#     -inverse
#     -homogeneous solutions..?
#     -non-homogeneous solutions..? (requires Vector class / 1 x self._m matrix)
#     - item assignement


class Matrix:

    def __init__(self, data):
        """Do NOT use. Use one of the constructors instead. (from2DList(),fromLists(),fromString(),fromInput())"""
        self.matrix = []
        self._m = len(data)
        self._n = len(data[0])
        self.transposed = False
        self._inversed = None
        self._rank = -1
        self._ref = None

        for i in range(len(data)):
            self.matrix.append([])
            self.matrix[i] = data[i][:]

    # region ----FUNCTIONS----

    def toString(self):
        """Pretty-prints the Matrix"""
        def centerText(text, charCount):
            textLen = len(text)
            beforeSpacesCount = floor((charCount - textLen)/2)
            afterSpacesCount = ceil((charCount - textLen)/2)
            return beforeSpacesCount * " " + text + afterSpacesCount * " "

        if self.matrix == self._ref:
            final = "\n-- Matrix (REF) --\n"
        else:
            final = "\n-- Matrix --\n"

        flatMatrix = [str(unit) for row in self.matrix for unit in row]
        allUnitCharCount = len(max(flatMatrix, key=len))

        for i in range(self._m):
            row = "| "
            for j in range(self._n):
                row += centerText(str(self.matrix[i][j]),
                                  allUnitCharCount) + " "

            if i == 0 and self.transposed:
                final += row[:-1] + f" |T\n"
            else:
                final += row[:-1] + f" |\n"

        return final[:-1]

    def rank(self):

        if self._rank == -1:
            self.ref()

        return self._rank

    def __getitem__(self, indexTuple):  # MATRIX[i,j] - tuple indexing
        """Matrix[i,j] -> Fraction/int on [i,j]th index """
        i, j = indexTuple
        if i > self._m or j > self._n:
            raise IndexError("Index of matrix is out of range.")

        return self.matrix[i-1][j-1]

    def refOld(self):

        if self._ref != None:
            return Matrix(self._ref)

        def findFirstNonZeroUnit(row):
            for i in range(len(row)):
                if row[i] != 0:
                    return i
            return len(row)

        # najdi na kazdym radku prvni nenulovou vec, podle sloupce ho jebni do jDict
        newMatrix = []
        jDict = dict()
        for row in self.matrix:
            index = findFirstNonZeroUnit(row)
            try:
                jDict[index].append(row)
            except KeyError:
                jDict[index] = []
                jDict[index].append(row)

        # projed kazdej sloupec
        for key in range(0, self._n):
            try:
                # spocitej kolik je radku s takovym pivotem
                rowCount = len(jDict[key])
            except KeyError:
                continue
            while rowCount > 1:
                # pokud vic nez jeden, pickni dva
                rowOne = jDict[key][0]
                rowTwo = jDict[key][1]

                #pickni jejich pivoty

                rowOneFirstNum = rowOne[key]
                rowTwoFirstNum = rowTwo[key]



                if rowOneFirstNum < 0:
                    rowOneFirstNum *= -1
                    rowTwoFirstNum *= -1

                coef = Fraction(-rowTwoFirstNum /
                                rowOneFirstNum).limit_denominator()

                multipliedRowOne = [(rowOneUnit * coef)
                                    for rowOneUnit in rowOne]

                newRowTwo = []
                for i in range(len(rowTwo)):
                    newRowTwo.append(rowTwo[i] + multipliedRowOne[i])

                jDict[key].pop(1)

                newIndex = findFirstNonZeroUnit(newRowTwo)

                try:
                    jDict[newIndex].append(newRowTwo)
                except KeyError:
                    jDict[newIndex] = []
                    jDict[newIndex].append(newRowTwo)

                rowCount = len(jDict[key])

        sortedKeys = sorted(jDict.keys())
        self._rank = len(sortedKeys)
        if self._n in sortedKeys:
            self._rank -= 1
        for key in sortedKeys:
            for row in jDict[key]:
                newMatrix.append(row)

        self._ref = newMatrix
        returningMatrix = Matrix(newMatrix)
        returningMatrix._rank = self._rank
        returningMatrix._ref = newMatrix
        
        return returningMatrix

    def WIP_refNew(self):

        if self._ref != None:
            return Matrix(self._ref)

        def findFirstNonZeroUnit(row):
            for i in range(len(row)):
                if row[i] != 0:
                    return i
            return len(row)

        unitMatrix = []
        for i in range(self._m):
            unitMatrix.append([])
            for j in range(self._n):
                unitMatrix[i].append(0)

        for i in range(self._m):
            unitMatrix[i][i] = 1

        pivotDict = dict()





    def inversed(self):

        if self._m != self._n:
            raise Exception("Inversed matrix is defined only for square matrices.")

        if not self._ref: self.ref()         
   
        if self._rank != self._m:
            raise Exception("This matrix is singular, inverse matrix doesn't exist.")

        
        
        

    # endregion

    # region ----MATH OPERATIONS----

    def _add(self, other, self_assign=False):
        if type(other) != Matrix:
            raise Exception("You can only add another matrix to this matrix.")
        if self._n != other._n or self._m != other._m:
            raise Exception(
                "Matrix addition is only defined for two matrices of the same size.")

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
                    final.append(self.matrix[row]
                                 [col] + other.matrix[row][col])
            return Matrix(final)

    def __add__(self, other):  # MATRIX+MATRIX
        """"""
        return self._add(other)

    def _constantMult(self, val):
        newMatrix = []

        for i in range(len(self.matrix)):
            newMatrix.append(self.matrix[i][:])
            for j in range(len(newMatrix[i])):
                newMatrix[i][j] *= val

        return Matrix(newMatrix)

    def _matrixMult(self, other):

        final = []

        if self._n != other._m:
            raise Exception(
                "Left matrices' column count doesn't equal right matrices' row count. Matrix multiplication is not defined")

        for i in range(self._m):
            final.append([])
            for j in range(other._n):
                final[i].append(0)
                for k in range(self._n):
                    final[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(final)

    def __mul__(self, val):  # n*MATRIX / MATRIX*MATRIX
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

    def __invert__(self):  # tilde(~)MATRIX - calls _transposed - Transposes Matrix
        return self._transposed()

    # endregion

    # ----CONSTRUCTORS----

    @staticmethod
    # DEFAULTS - rowSplitChar = "@" colSplitChar = "&"
    def fromString(matrixString, rowSplitChar="@", colSplitChar="&"):

        finalList = []

        rows = matrixString.split(rowSplitChar)
        n = len(rows[0].split(colSplitChar))

        for i in range(len(rows)):
            units = rows[i].split(colSplitChar)

            if len(units) != n:
                raise Exception("All rows must have the same number of units.")

            finalList.append([Fraction(str(unit)).limit_denominator()
                             for unit in units])

        return Matrix(finalList)

    @staticmethod
    def fromLists(*matrixLists):
        finalList = []
        n = len(matrixLists[0])

        for lst in matrixLists:
            if len(lst) != n:
                raise Exception("All rows must have the same number of units.")

            finalList.append(
                [Fraction(str(unit)).limit_denominator() for unit in lst])

        return Matrix(finalList)

    @staticmethod
    def from2DList(matrixList):
        finalList = []
        n = len(matrixList[0])

        for row in matrixList:

            if len(row) != n:
                raise Exception("All rows must have the same number of units.")

            finalList.append(
                [Fraction(str(unit)).limit_denominator() for unit in row])

        return Matrix(finalList)

    @staticmethod
    def fromInput():  # unlike other constructors requires user input
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


# a = Matrix.from2DList([[3, 4, 3], [2, 4, 4], [1, 2, 2]])
# os.system("cls||clear")
# print("default matrix A")

# print(a.toString())

# input("...")
# # os.system("cls||clear")
# print("A in REF")

# print(a.ref().toString())

# input("...")
# # os.system("cls||clear")

# print("rank(A)")

# print(a.rank())

# input("...")
# # os.system("cls||clear")


# aT = ~a
# print("(A)T")
# print(aT.toString())
