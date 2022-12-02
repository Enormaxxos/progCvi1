from MatrixClass import Matrix

a = Matrix.from2DList([[2,3],[3,4]])
b = Matrix.from2DList([[4,6],[5,7]])
const = 5

aTimesConst = a * const
abProd = a * b
baProd = b * a

print("Constant multiplication: ")
print(aTimesConst)
print("________")

print("Product of both matrices: ")
print(abProd)
print("________")

print("Product of both matrices in switched order: ")
print(baProd)
