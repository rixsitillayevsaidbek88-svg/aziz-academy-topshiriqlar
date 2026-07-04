n = int(input())
if n <= 1:
    print("yo'q")
else:
    bo_lunuvchi = 2
    tub = True
    while bo_lunuvchi * bo_lunuvchi <= n:
        if n % bo_lunuvchi == 0:
            tub = False
            break
        bo_lunuvchi += 1
    if tub:
        print("ha")
    else:
        print("yo'q")