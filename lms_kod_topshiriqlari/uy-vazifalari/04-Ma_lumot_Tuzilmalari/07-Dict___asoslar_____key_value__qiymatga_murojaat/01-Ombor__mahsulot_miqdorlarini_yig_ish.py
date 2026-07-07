n = int(input())
ombor = {}
for _ in range(n):
    nomi, miqdori = input().split()
    miqdori = int(miqdori)
    
    if nomi in ombor:
        ombor[nomi] += miqdori
    else:
        ombor[nomi] = miqdori
for nomi, jami in ombor.items():
    print(nomi, jami)