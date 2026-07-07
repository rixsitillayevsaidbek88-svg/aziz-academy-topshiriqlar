n = int(input())
oquvchilar = []
bahoy = 0
for _ in range(n):
    ism, baho = input().split()
    baho = int(baho)
    oquvchilar.append({"ism": ism, "baho": baho})
    bahoy += baho
ortacha = bahoy / n
for bola in oquvchilar:
    if bola["baho"] > ortacha:
        print(bola["ism"])