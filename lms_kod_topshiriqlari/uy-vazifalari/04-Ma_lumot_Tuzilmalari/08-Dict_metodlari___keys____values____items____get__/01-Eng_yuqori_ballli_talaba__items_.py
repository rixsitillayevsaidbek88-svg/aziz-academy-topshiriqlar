n = int(input())
tes = {}
for i in range(n):
    ism, baho = input().split()
    baho = int(baho)
    tes[ism] = baho
eng = sorted(tes.items(), key=lambda x: (-x[1], x[0]))[0]
print(f"{eng[0]} {eng[1]}")