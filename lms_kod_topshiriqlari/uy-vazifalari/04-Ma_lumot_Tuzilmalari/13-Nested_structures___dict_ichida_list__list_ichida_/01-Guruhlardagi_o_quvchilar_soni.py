n = int(input())
guruhlar = []

for _ in range(n):
    malumot = input().split()
    guruh_nomi = malumot[0]
    oqivchilar = malumot[1:]
    
    guruhlar.append({guruh_nomi: oqivchilar})
   

for guruh in guruhlar:
    for nomi, azolari in guruh.items():
        print(nomi, len(azolari))