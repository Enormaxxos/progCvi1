x = int(input('cislo v binarni soustave: '))

final = 0
i = 0

while x != 0:
    digit = x % 10 # ziskani posledni cislice zadaneho cisla
    x = x // 10 # zkraceni zadaneho cisla o posledni cislici
    final += digit * (2**i) #pricteni k vyslednemu cislu v desitkove soustave
    i += 1

print(final)
