year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Kabisa")
        else:
            print("Kabisa emas")
    else:
        print("Kabisa")
else:
    print("Kabisa emas")