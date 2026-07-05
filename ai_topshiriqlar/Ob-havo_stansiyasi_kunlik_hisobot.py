# Ob-havo stansiyasi: kunlik hisobot
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())

u = 0
j = 0

m -1
e = ""
for _ in range(n):
    q = input().split()
    nom = q[0]
    narx = int(q[1])
    soni = int(q[2])
    
    jo = narx * soni
    
    u += jo
    j += soni
    
    if jo > m:
        m = jo
        e = nom
print(u)
print(e)
print(j)