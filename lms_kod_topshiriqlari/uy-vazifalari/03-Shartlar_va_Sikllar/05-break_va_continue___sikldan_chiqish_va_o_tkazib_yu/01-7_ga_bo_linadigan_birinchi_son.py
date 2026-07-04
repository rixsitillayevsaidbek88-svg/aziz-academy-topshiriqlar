n = int(input())
sanoq = 0
topildi = False
while sanoq < n:
    son = int(input())
    sanoq += 1
    if son % 7 == 0:
        print(son)
        topildi = True
        break
if not topildi:
    print("yo'q")