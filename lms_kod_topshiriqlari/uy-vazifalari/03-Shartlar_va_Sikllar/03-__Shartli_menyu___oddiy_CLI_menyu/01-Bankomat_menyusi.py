amal = int(input())
balans = int(input())
summa = int(input())

if amal == 1:
    print(balans)
elif amal == 2:
    if summa <= balans:
        yangi = balans - summa
        print(yangi)
    else:
        print("Mablag' yetarli emas")
elif amal == 3:
    yangi = balans + summa
    print(yangi)