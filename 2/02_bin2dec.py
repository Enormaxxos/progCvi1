x = int(input())

final = 0
i = 0

while x != 0:
    digit = x % 10
    x = x // 10
    final += digit * (2**i)
    i += 1

print(str(final))
