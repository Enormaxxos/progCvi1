x = int(input())
n = int(input())

mocnina = 1

while n > 0:
    if n % 2 == 1:
        mocnina *= x
    x = x**2
    n = n//2

print(mocnina)