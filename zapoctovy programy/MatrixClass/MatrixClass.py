import os
from fractions import Fraction
from math import ceil, floor

#     -fromString constructor (& for columns, @ for rows) - DONE
#     -from2darray constructor - DONE
#     -fromArrays constructor - DONE
#     -fromInput interactive constructor - DONE
#     -toString() pretty-print - DONE
#     -matrix + matrix (addition) - DONE (plus sign)
#     -matrix * n (constant multiplication) - DONE (asterisk sign)
#     -matrix * matrix (matrix multiplication) - DONE (asterisk sign)
#     -transposition - mostly DONE (tilde sign, unar / Matrix.transposed() ... ?)
#     -REF tvar - DONE
#     -rank - DONE
#     -inverse - DONE
#     -determinant - DONE
#     -TODO:huge bug testing
#     -TODO:documentation (.md file)


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

    def __str__(self):
        """Pretty-prints the Matrix"""
        def centerText(text, charCount):
            textLen = len(text)
            beforeSpacesCount = floor((charCount - textLen)/2)
            afterSpacesCount = ceil((charCount - textLen)/2)
            return beforeSpacesCount * " " + text + afterSpacesCount * " "

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

    def ref(self, **kwargs):

        # pokud uz byla spocitana, a nezavola si to inverted(), vrat matici
        if self._ref != None and "_invCall" not in kwargs.keys():
            return Matrix(self._ref)

        def findFirstNonZeroUnit(row):
            for i in range(len(row)):
                if row[i] != 0:
                    return i
            return None

        # vytvor jednotkovou matici stejneho radu
        unitMatrix = []
        for i in range(self._m):
            unitMatrix.append([])
            for j in range(self._n):
                unitMatrix[i].append(Fraction(0, 1))

        for i in range(self._m):
            unitMatrix[i][i] = Fraction(1, 1)

        # zkopiruj si data matice do temporary var, aby se neupravovaly data na hlavni neznamy matice
        temp = []
        for row in self.matrix:
            temp.append(row[:])

        looping = True

        # opakuj dokud existujou aspon dva radky na jakymkoliv pivotu
        while looping:
            looping = False
            pivots = dict()  # {j s pivotem : i radku}

            for i in range(self._m):
                rowPivotIndex = findFirstNonZeroUnit(temp[i])
                if rowPivotIndex == None:
                    continue

                try:
                    pivots[rowPivotIndex].append(i)
                except KeyError:
                    pivots[rowPivotIndex] = []
                    pivots[rowPivotIndex].append(i)

            sortedPivots = sorted(pivots.keys())

            for pivot in sortedPivots:
                if len(pivots[pivot]) <= 1:
                    continue

                looping = True

                rowOneIndex = pivots[pivot][0]
                rowOne = temp[rowOneIndex][:]
                unitMatrixRowOne = unitMatrix[rowOneIndex][:]
                rowOnePivotVal = temp[rowOneIndex][pivot]

                rowTwoIndex = pivots[pivot][1]
                rowTwo = temp[rowTwoIndex][:]
                unitMatrixRowTwo = unitMatrix[rowTwoIndex][:]
                rowTwoPivotVal = temp[rowTwoIndex][pivot]

                if rowOnePivotVal < 0:
                    rowOnePivotVal *= -1
                    rowTwoPivotVal *= -1

                coef = Fraction(rowTwoPivotVal /
                                rowOnePivotVal).limit_denominator()

                multRowOne = [unit * coef for unit in rowOne]
                multUnitMatrixRowOne = [
                    unit * coef for unit in unitMatrixRowOne]

                subtrRowTwo = [rowTwo[i] - multRowOne[i]
                               for i in range(len(rowTwo))]
                subtrUnitMatrixRowTwo = [
                    unitMatrixRowTwo[i] - multUnitMatrixRowOne[i] for i in range(len(unitMatrixRowTwo))]

                temp[rowTwoIndex] = subtrRowTwo
                unitMatrix[rowTwoIndex] = subtrUnitMatrixRowTwo

        self._rank = len(pivots)
        self._ref = temp

        if '_invCall' not in kwargs.keys():
            newMatrix = Matrix(temp)
            newMatrix._rank = self._rank
            newMatrix._ref = self._ref
            # newMatrix._canBe
            return newMatrix
        else:
            return temp, unitMatrix

    def inversed(self):

        if self._inversed != None:
            return Matrix(self._inversed)

        if self._m != self._n:
            raise Exception(
                "Inversed matrix is defined only for square matrices.")

        mainMatrix, invMatrix = self.ref(_invCall=True)

        mainMatrix = mainMatrix.copy()
        mainMatrix = [row.copy() for row in mainMatrix]

        if self._rank != self._m:
            raise Exception(
                "This matrix is singular, inverse matrix doesn't exist.")

        for i in range(len(mainMatrix)-1, -1, -1):
            for j in range(i-1, -1, -1):
                rowDown = mainMatrix[i][:]
                invRowDown = invMatrix[i][:]

                rowUp = mainMatrix[j][:]
                invRowUp = invMatrix[j][:]

                rowUpVal = rowUp[i]
                rowDownVal = rowDown[i]

                if rowDownVal < 0:
                    rowDownVal *= -1
                    rowUpVal *= -1

                coef = Fraction(rowUpVal / rowDownVal).limit_denominator()

                multRowDown = [unit * coef for unit in rowDown]
                multInvRowDown = [unit * coef for unit in invRowDown]

                subtrRowUp = [rowUp[pos] - multRowDown[pos]
                              for pos in range(len(rowUp))]
                subtrInvRowUp = [invRowUp[pos] - multInvRowDown[pos]
                                 for pos in range(len(invRowUp))]

                # TENHLE RADEK FUCKUPUJE SELF._REF. stejnej pointer, zkopirovat listy, zmenit adresy
                mainMatrix[j] = subtrRowUp
                invMatrix[j] = subtrInvRowUp

            coef = mainMatrix[i][i]

            mainMatrix[i][i] = Fraction(
                mainMatrix[i][i] / coef).limit_denominator()
            invMatrix[i] = [invMatrix[i][pos] *
                            (1/coef) for pos in range(len(invMatrix[i]))]

        self._inversed = invMatrix

        return Matrix(invMatrix)

    def determinant(self):

        if self._m != self._n:
            raise Exception("Determinant is defined only for square matrices.")

        def detRecursive(matrix):
            if len(matrix) == 1:
                return matrix[0][0]

            final = 0

            for i in range(len(matrix)):
                newMatrix = []

                for j in range(1,len(matrix)):
                    newMatrix.append([])

                    for k in range(len(matrix)):
                        if k == i:
                            continue

                        newMatrix[j-1].append(matrix[j][k])

                final += ((-1)**i) * matrix[0][i] * detRecursive(newMatrix)

            return final

        return detRecursive(self.matrix)
    # endregion

    # region ----MATH OPERATIONS----

    def _add(self, other):
        if type(other) != Matrix:
            raise Exception("You can only add another matrix to this matrix.")
        if self._n != other._n or self._m != other._m:
            raise Exception(
                "Matrix addition is only defined for two matrices of the same size.")

        final = []
        for row in range(self._m):
            final.append([])

            for col in range(self._n):
                final[row].append(self.matrix[row]
                                [col] + other.matrix[row][col])
        print(final)
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
        if type(val) == int or type(val) == float or type(val) == Fraction:
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
        if len(row) == 0:
            raise Exception("Aborting, no data given")
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


# a = Matrix.fromString("2&3&4@7&2&4@8&5&2")

# c = a*5

# print(c)
