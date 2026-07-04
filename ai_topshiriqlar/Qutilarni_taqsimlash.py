# Qutilarni taqsimlash
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

# Yechimingizni shu yerga yozing
# Kirish: input(), chiqish: print()
N = int(input())
K = int(input())
ulash = N // K
qoldiq = N % K
y = (K - qoldiq) % K if qoldiq != 0 else 0
print(ulash)
print(qoldiq)
print(y)