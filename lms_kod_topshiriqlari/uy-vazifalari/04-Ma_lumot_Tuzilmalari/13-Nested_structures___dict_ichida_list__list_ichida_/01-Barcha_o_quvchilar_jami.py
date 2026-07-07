n = int(input())
guruhlar = []
jami_oqi = 0
for _ in range(n):
    malumot = input().split()
    guruh_nomi = malumot[0]
    oqiv = malumot[1:]
    
    guruhlar.append({guruh_nomi: oqiv})

for guruh in guruhlar:
    for azolar in guruh.values():
        jami_oqi += len(azolar)
        
print(jami_oqi)