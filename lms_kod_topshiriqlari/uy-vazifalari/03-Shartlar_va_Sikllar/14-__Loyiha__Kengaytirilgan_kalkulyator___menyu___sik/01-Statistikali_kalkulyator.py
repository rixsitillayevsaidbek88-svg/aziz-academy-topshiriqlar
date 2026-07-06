amallar = 0
natija = 0
while True:
    amal = int(input())
    if amal == 0:
        break
    a = int(input())
    b = int(input())
    yaroqli = False
    jori = 0
    if amal == 1:
        jori = a + b
        yaroqli = True
    elif amal == 2:
        jori = a - b
        yaroqli = True
    elif amal == 3:
        jori = a * b
        yaroqli = True
    elif amal == 4:
        if b != 0:
            jori = a // b
            yaroqli = True
    if yaroqli:
        print(jori)
        amallar += 1
        natija += jori
print(f"Amallar: {amallar}")
print(f"Natijalar yig'indisi: {natija}")