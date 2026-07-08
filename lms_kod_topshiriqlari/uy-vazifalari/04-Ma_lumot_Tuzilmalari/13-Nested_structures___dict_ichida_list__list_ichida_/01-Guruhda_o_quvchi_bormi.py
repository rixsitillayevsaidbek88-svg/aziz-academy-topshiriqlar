n = int(input())
guruhlar = {}
for i in range(n):
    guruh_nomi, *oqivchilar = input().split()
    guruhlar[guruh_nomi] = oqivchilar
    
guruh_nomi, qidiriladigan = input().split()
if qidiriladigan in guruhlar[guruh_nomi]:
    print("Ha")
else:
    print("Yoq")