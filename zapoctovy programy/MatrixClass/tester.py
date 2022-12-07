from MatrixClass import Matrix
from fractions import Fraction
import random

def genMatrix():
    matrix = []

    isSquare = True

    matN = random.randrange(1,4)
    if isSquare:
        matM = matN
    else:
        matM = random.randrange(1,4)

    for i in range(matM):
        matrix.append([])
        for j in range(matN):
            fracNum = random.randrange(21)
            isFraction = False
            if isFraction:
                fracDen = random.randrange(1,21)
            else:
                fracDen = 1
            matrix[i].append(Fraction(numerator=fracNum,denominator=fracDen))

    print("matrix definition =",matrix)

    return Matrix.from2DList(matrix)

for i in range(30):
    A = genMatrix()
    if A._n == A._m:
        print("SQAURE Matrix A")
    else:
        print("Matrix A")
    print(A)
    print("----")
    print("Matrix A in REF")
    print(A.ref())
    print("----")
    print("Rank of matrix A =",A.rank())
    print("----")

    try:
        print("Matrix inversed")
        AInv = A.inversed()
        print(AInv)
        print("----")
        print("Matrix A * Matrix A inversed")
        print(A * AInv)
    except Exception:
        print("Matrix cannot be inversed.")
    print("=====")


