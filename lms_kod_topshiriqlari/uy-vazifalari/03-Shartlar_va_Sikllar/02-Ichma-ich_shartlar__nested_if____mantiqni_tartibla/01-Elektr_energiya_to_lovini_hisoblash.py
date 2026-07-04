a = int(input())

if a < 0:
    print("Notogri qiymat")
else:
    if a <= 100:
        summa = a * 450
    elif a <= 200:
        summa = (100 * 450) + ((a - 100) * 600)
    else:
        summa = (100 * 450) + (100 * 600) + ((a - 200) * 900)
    
    print(summa)