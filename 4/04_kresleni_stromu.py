a = int(input())
b = int(input())

def strom(k,l):
    final = ""

    for i in range(k):
        line = ""
        line += (k-i-1)*"."
        line += (i*2 + 1)*"*"
        line += (k-i-1)*"."
        final += line + "\n"

    for i in range(l):
        line = ""
        line += (k-1)*"."
        line += "*"
        line += (k-1)*"."
        final += line + ("\n" if i != l-1 else "")
    
    return final

print(strom(a,b))