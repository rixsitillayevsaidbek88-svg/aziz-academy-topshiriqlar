n = int(input())
ovozlar = {}
golib = ""
maks_ovoz = 0
for _ in range(n):
    ism = input()
    if ism in ovozlar:
        ovozlar[ism] += 1
    else:
        ovozlar[ism] = 1
    if ovozlar[ism] > maks_ovoz:
        maks_ovoz = ovozlar[ism]
        golib = ism
print(golib)