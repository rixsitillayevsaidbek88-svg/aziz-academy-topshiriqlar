start = int(input())
step = int(input())
if step <= 0:
    print("CHEKSIZ")
else:
    qadamlar = 0
    while start < 100:
        start += step
        qadamlar += 1
    print(qadamlar)