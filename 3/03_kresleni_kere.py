a = int(input())

final = ""

for i in range(a):
    line = ""
    line += (a-i-1)*"."
    line += (i*2 + 1)*"*"
    line += (a-i-1)*"."
    final += line + ("\n" if i < a-1 else "")

print(final)