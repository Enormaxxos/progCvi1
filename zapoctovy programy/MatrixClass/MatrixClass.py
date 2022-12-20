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
#     -testing file - DONE
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

        # funkce centerujici hodnoty v matici kvuli prehlednosti
        def centerText(text, charCount):
            textLen = len(text)
            beforeSpacesCount = floor((charCount - textLen)/2)
            afterSpacesCount = ceil((charCount - textLen)/2)
            return beforeSpacesCount * " " + text + afterSpacesCount * " "

        final = "-- Matrix --\n"


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

    def __eq__(self, other):
        """Checks if sizes of matrices equal, then checks if numbers in them equal"""
        if self._m != other._m and self._n != other._n:
            return False

        final = True
        for i in range(self._m):
            for j in range(self._n):
                if self.matrix[i][j] != other.matrix[i][j]:
                    final = False
                    c = False
                    break
            if not final:
                break

        return final

    def rank(self):
        """Returns rank (number of pivots in REF) of matrix"""

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
        """Returns matrix in REF, also pre-calculates rank of matrix"""
        # funkci ref si interne vyvolava i funkce .inversed() kvuli pocatecnim upravam

        # pokud uz byla ref spocitana, a funkci si nezavola .inverted(), vrat matici
        if self._ref != None and "_invCall" not in kwargs.keys():
            return Matrix(self._ref)

        # funkce hledajici prvni nenulove cislo v zadanem radku
        def findFirstNonZeroUnit(row):
            for i in range(len(row)):
                if row[i] != 0:
                    return i
            return None

        # vytvor jednotkovou matici stejneho radu kvuli callu .inversed()
        if self._n == self._m:
            unitMatrix = []
            for i in range(self._m):
                unitMatrix.append([])
                for j in range(self._n):
                    unitMatrix[i].append(Fraction(0, 1))

            for i in range(self._m):
                unitMatrix[i][i] = Fraction(1, 1)

        # zkopiruj si data matice do temporary var, aby se kvuli stejnemu odkazu neupravovaly data na hlavni neznamy matice
        temp = []
        for row in self.matrix:
            temp.append(row[:])

        looping = True

        # opakuj dokud existujou libovolny dva radky s pivotem na stejnem sloupci
        while looping:
            looping = False
            pivots = dict()  # {j s pivotem : i radku}

            # vytvor si dictionary s tvarem {j s pivotem : [i radku s pivotem na j-te pozici, i dalsiho takoveho radku,...]}
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

            # zacni prohledavat od pivotu nejvice vlevo, pokud se dva radky rovnaji v J jeho pivotu, proved vypocet
            for pivot in sortedPivots:
                if len(pivots[pivot]) <= 1:
                    continue

                looping = True

                # najdi hodnotu pivotu v hornim radku
                rowOneIndex = pivots[pivot][0]
                rowOne = temp[rowOneIndex][:]
        finalList = []
                if self._n == self._m:
                    unitMatrixRowOne = unitMatrix[rowOneIndex][:]
                rowOnePivotVal = temp[rowOneIndex][pivot]

                # najdi hodnotu pivotu ve spodnim radku
                rowTwoIndex = pivots[pivot][1]
                rowTwo = temp[rowTwoIndex][:]
                if self._n == self._m:
                    unitMatrixRowTwo = unitMatrix[rowTwoIndex][:]
                rowTwoPivotVal = temp[rowTwoIndex][pivot]

                if rowOnePivotVal < 0:
                    rowOnePivotVal *= -1
                    rowTwoPivotVal *= -1

                # hodnoty pivotu vydel -> koeficient, kterym se nasobi prvni radek
                coef = Fraction(rowTwoPivotVal /
                                rowOnePivotVal)

                # vynasob prvni radek
                multRowOne = [unit * coef for unit in rowOne]
                if self._n == self._m:
                    multUnitMatrixRowOne = [
                        unit * coef for unit in unitMatrixRowOne]

                # odecti od druheho radku vynasobeny prvni radek
                subtrRowTwo = [rowTwo[i] - multRowOne[i]
                               for i in range(len(rowTwo))]
                if self._n == self._m:
                    subtrUnitMatrixRowTwo = [
                        unitMatrixRowTwo[i] - multUnitMatrixRowOne[i] for i in range(len(unitMatrixRowTwo))]

                # puvodni radek prepis novym vypoctenym radkem
                temp[rowTwoIndex] = subtrRowTwo
                if self._n == self._m:
                    unitMatrix[rowTwoIndex] = subtrUnitMatrixRowTwo

        # serad radky podle pivotu
        pivots = dict()
        for i in range(self._m):
            rowPivotIndex = findFirstNonZeroUnit(temp[i])
            if rowPivotIndex == None:
                continue

            try:
                pivots[rowPivotIndex].append(temp[i])
            except KeyError:
                pivots[rowPivotIndex] = []
                pivots[rowPivotIndex].append(temp[i])

        sortedPivots = sorted(pivots)

        temp = []
        for pivot in sortedPivots:
            for line in pivots[pivot]:
                temp.append(line)

        self._rank = len(pivots)
        self._ref = temp

        # pokud si tuto funkci zavolal uzivatel, vrat pouze upravenou puvodni matici 
        if '_invCall' not in kwargs.keys():
            newMatrix = Matrix(temp)
            newMatrix._rank = self._rank
            newMatrix._ref = self._ref
            # newMatrix._canBe
            return newMatrix
        # pokud si ji zavola funkce .inversed(), vrat upravenou puvodni matici spolecne s doposud upravenou jednotkovou matici 
        else:
            return temp, unitMatrix

    def inversed(self):
        """Finds inversed matrix of given matrix, if one exists"""

        # pokud jiz byla spocitana, vrat ji
        if self._inversed != None:
            return Matrix(self._inversed)

        # pokud neni matice ctvercova, inverzni neexistuje
        if self._m != self._n:
            raise Exception(
                "Inversed matrix is defined only for square matrices.")

        # zavolej si funkci .ref() -> matice v ref a castecne upravena jednotkova matice
        mainMatrix, invMatrix = self.ref(_invCall=True)

        # zkopiruj si matici do temp nezname, aby se neupravovala hlavni neznama matice se stejnym linkem
        mainMatrix = mainMatrix.copy()
        mainMatrix = [row.copy() for row in mainMatrix]

        # pokud je rank < rad matice, inverzni matice neexistuje
        if self._rank != self._m:
            raise Exception(
                "This matrix is singular, inverse matrix doesn't exist.")

        # po Gaussove eliminaci zacni provadet Gauss-Jordanovu eliminaci
        for i in range(len(mainMatrix)-1, -1, -1):
            for j in range(i-1, -1, -1):
                # i-ty radek vynasob vhodnym koeficientem, odecti ho od kazdeho radku nad nim, zacni odspoda
                rowDown = mainMatrix[i][:]
                invRowDown = invMatrix[i][:]

                rowUp = mainMatrix[j][:]
                invRowUp = invMatrix[j][:]

                rowUpVal = rowUp[i]
                rowDownVal = rowDown[i]

                if rowDownVal < 0:
                    rowDownVal *= -1
                    rowUpVal *= -1

                coef = Fraction(rowUpVal / rowDownVal)

                multRowDown = [unit * coef for unit in rowDown]
                multInvRowDown = [unit * coef for unit in invRowDown]

                subtrRowUp = [rowUp[pos] - multRowDown[pos]
                              for pos in range(len(rowUp))]
                subtrInvRowUp = [invRowUp[pos] - multInvRowDown[pos]
                                 for pos in range(len(invRowUp))]

                mainMatrix[j] = subtrRowUp
                invMatrix[j] = subtrInvRowUp

            coef = mainMatrix[i][i]

            mainMatrix[i][i] = Fraction(
                mainMatrix[i][i] / coef).limit_denominator()
            invMatrix[i] = [(invMatrix[i][pos] *
                            (1/coef)) for pos in range(len(invMatrix[i]))]

        # zkrat nehezke zlomky pro prehlednost
        for i in range(len(invMatrix)):
            for j in range(len(invMatrix[i])):
                invMatrix[i][j].limit_denominator()

        self._inversed = invMatrix

        return Matrix(invMatrix)

    def determinant(self):
        """Finds determinant of given matrix (returns 0 for singular matrices, non-zero for regular matrices)"""

        # determinant nelze vypocitat, pokud matice neni ctvercova
        if self._m != self._n:
            raise Exception("Determinant is defined only for square matrices.")

        # priklad, jak funguje rekurzivni funkce detRecursive()
        #   | a b c |
        # A=| d e f | -> det(A) = a * det | e f | - b * det | d f | + c * det | d e |
        #   | g h i |                     | h i |           | g i |           | g h |
        def detRecursive(matrix):
            if len(matrix) == 1:
                return matrix[0][0]

            final = 0

            for i in range(len(matrix)):
                newMatrix = []

                for j in range(1, len(matrix)):
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
        """DO NOT USE: internal function, use Matrix + Matrix instead."""

        # zkontroluj podminky nutne pro secteni matic (druhy operand je matice, rady se rovnaji)
        if type(other) != Matrix:
            raise Exception("You can only add another matrix to this matrix.")
        if self._n != other._n or self._m != other._m:
            raise Exception(
                "Matrix addition is only defined for two matrices of the same size.")

        # pro kazde i,j secti Ai,j a Bi,j, nastav ho na i,j pozici nove matice
        final = []
        for row in range(self._m):
            final.append([])

            for col in range(self._n):
                final[row].append(self.matrix[row]
                                  [col] + other.matrix[row][col])
        return Matrix(final)

    def __add__(self, other):  # MATRIX+MATRIX
        """Matrix addition -> (A+B)i,j = Ai,j + Bi,j"""
        return self._add(other)

    def _constantMult(self, val):
        """DO NOT USE: internal function, use Matrix * constant instead"""
        newMatrix = []

        # kazdou hodnotu matice vynasob zadanou konstantou, vrat novou matici
        for i in range(len(self.matrix)):
            newMatrix.append(self.matrix[i][:])
            for j in range(len(newMatrix[i])):
                newMatrix[i][j] *= val

        return Matrix(newMatrix)

    def _matrixMult(self, other):
        """DO NOT USE: internal function, use Matrix * Matrix instead"""
        final = []

        # zkontroluj rady matic, pocet sloupcu leve matice se musi rovnat poctu radku prave matice
        if self._n != other._m:
            raise Exception(
                "Left matrices' column count doesn't equal right matrices' row count. Matrix multiplication is not defined")
 
        for i in range(self._m):
            final.append([])
            for j in range(other._n):
                final[i].append(Fraction(0, 1))
                for k in range(self._n):
                    final[i][j] += self.matrix[i][k] * other.matrix[k][j]
                    final[i][j].limit_denominator()

        return Matrix(final)

    def __mul__(self, val):  # n*MATRIX / MATRIX*MATRIX
        """Matrix/constant multiplication -> (Matrix * Matrix) - matrix multiplication, (Matrix * constant) - constant multiplication"""
        if type(val) == int or type(val) == float or type(val) == Fraction:
            return self._constantMult(Fraction(val).limit_denominator())
        if type(val) == Matrix:
            return self._matrixMult(val)

    def _transposed(self):
        """DO NOT USE: internal function, use ~Matrix instead"""

        # inicializace neznamych
        newMatrixList = []
        self.newN = self._m
        self.newM = self._n

        # hodnotu na i,j-pozici nastav ja j,i-pozici nove matice, vrat novou matici
        for i in range(self.newM):
            newMatrixList.append([])
            for j in range(self.newN):
                newMatrixList[i].append(self.matrix[j][i])

        newMatrix = Matrix(newMatrixList)
        #nastav .transposed na opacnou hodnotu, kvuli Pretty-printu
        newMatrix.transposed = not self.transposed

        return newMatrix

    def __invert__(self):  # tilde(~)MATRIX - calls _transposed - Transposes Matrix
        """Returns transposed matrix -> Ai,j = ATj,i"""
        return self._transposed()

    # endregion

    # ----CONSTRUCTORS----

    @staticmethod
    # DEFAULTS - rowSplitChar = "@" colSplitChar = "&"
    def fromString(matrixString, rowSplitChar="@", colSplitChar="&"):
        """Creates a new instance of Matrix. Default separator for columns is ampersand (&), default separator for rows is At sign (@)"""

        finalList = []

        # rozdel si zadany string na radky pomoci rowSplit charakteru, nastav si neznamou n pro kontrolu delky radku
        rows = matrixString.split(rowSplitChar)
        n = len(rows[0].split(colSplitChar))

        for i in range(len(rows)):
            units = rows[i].split(colSplitChar)

            # pokud se nerovnaji vsechny radky ve sve delce, vyvolej chybu - matice musi mit stejny pocet hodnot v kazdem radku
            if len(units) != n:
                raise Exception("All rows must have the same number of units.")

            # zkrat zlomky hodnot, vrat novou matici
            finalList.append([Fraction(str(unit)).limit_denominator()
                             for unit in units])

        return Matrix(finalList)

    @staticmethod
    def fromLists(*matrixLists):
        """Creates a new instance of Matrix. Parameters are individual rows of a new matrix."""
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
        """Creates a new instance of Matrix. Only parameter is 2D list, with each sublist being row."""

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
        """Interactively creates a new instance of matrix. Requires user input in console. Use for debugging."""

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

    @staticmethod
    def createUnit(n):
        """Creates a new instance of a unit matrix. Only parameter is size of matrix."""
        newMatrix = []

        for i in range(n):
            newMatrix.append([])
            for j in range(n):
                newUnit = Fraction(1, 1) if i == j else Fraction(0, 1)
                newMatrix[i].append(newUnit)

        return Matrix(newMatrix)


if __name__ == "__main__":
    A = Matrix.from2DList([[18, 6, 3], [3, 1, 13], [5, 8, 5]])
    # AInv = A.inversed()

    B = Matrix.from2DList([[18, 6, 3], [5, 8, 5], [3, 1, 13]])
    BInv = B.inversed()
