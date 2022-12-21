# tests some MatrixClass functions
# after tests dumps wrong answers to dump.txt (if needed)

from MatrixClass import Matrix
from fractions import Fraction
import random
import argparse

def genMatrix():
    matrix = []

    isSquare = True

    matN = random.randrange(1,7)
    if isSquare:
        matM = matN
    else:
        matM = random.randrange(1,4)

    for i in range(matM):
        matrix.append([])
        for j in range(matN):
            fracNum = random.randrange(1,21)
            isFraction = False
            if isFraction:
                fracDen = random.randrange(1,21)
            else:
                fracDen = 1
            matrix[i].append(Fraction(numerator=fracNum,denominator=fracDen))

    # print("matrix definition =",matrix)

    return Matrix.from2DList(matrix)

def testDoubleTranspose(testC):

    testCount = 0
    correctCount = 0

    wrongList = []

    with open("dump.txt","w") as o:
        o.write("============DOUBLE TRANSPOSE TESTING============\n")
        for i in range(testC):
            A = genMatrix()
            ATrans = ~A
            ATransTrans = ~ATrans

            testCount += 1
            if A == ATransTrans:
                correctCount += 1
            else:
                o.write(f"Matrix :\n{A.__str__()}\n------\nATrans :\n{ATrans}\n------\nATransTrans:\n{ATransTrans}\n======")
                wrongList.append(A)

    print("===DOUBLE TRANSPOSE TESTING=====")

    print("testCount =",testCount)
    print("correctCount =",correctCount)
    print("percentage of success =", round((correctCount/testCount)*100,3),"%")

def testInverseMatrix(testC):

    testCount = 0
    correctCount = 0

    wrongList = []

    with open("dump.txt","w") as o:
        o.write("============INVERSE MATRIX TESTING============\n")
        for i in range(testC):
            A = genMatrix()
            unit = Matrix.createUnit(A._n)
            try:
                AInv = A.inversed()
            except Exception:
                continue

            AInvTimesA = A * AInv
            testCount += 1
            if unit == AInvTimesA:
                correctCount += 1
            else:
                o.write(f"Matrix :\n{A.__str__()}\n------\nAInv :\n{AInv}\n------\nAInvTimesA:\n{AInvTimesA}\n======")
                wrongList.append(A)

    print("===INVERSE MATRIX TESTING===")
    
    print("testCount =",testCount)
    print("correctCount =",correctCount)
    print("percentage of success =", round((correctCount/testCount)*100,3),"%")

parser = argparse.ArgumentParser()

parser.add_argument("--test",dest="whatToTest")
parser.add_argument("--number",dest="numberOfTests")

args = parser.parse_args()

match args.whatToTest.lower():
    case "inverse":
        testInverseMatrix(int(args.numberOfTests))
    case "trans":
        testDoubleTranspose(int(args.numberOfTests))
    case A:
        print("Keyword unknown. Use 'Inverse' or 'Trans'.")

