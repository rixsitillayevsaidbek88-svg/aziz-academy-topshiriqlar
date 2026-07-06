# Davomiylikni hisoblash
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

a = int(input())
b = int(input())
c = int(input())
d = int(input())
bosh = a * 60 + b
tugash = c * 60 + d
farq = tugash - bosh
soat = farq // 60
daqiqa = farq % 60
print(soat)
print(daqiqa)