# Davomat tahlili
# Kurs: Dasturlash / IT
# Mavzu: O'rnatish va muhit — Python, interpreter, IDE sozlash
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
davomat = input().split()
kelgan_kunlar = davomat.count('1')
max_seriya = 0
joriy = 0
for kun in davomat:
    if kun == '1':
        joriy += 1
        if joriy > max_seriya:
            max_seriya = joriy
            
    else:
        joriy = 0
davomat_f = (kelgan_kunlar * 100) // n
print(kelgan_kunlar)
print(max_seriya)
print(davomat_f)