n = int(input())
talabalar = []
for _ in range(n):
    satr = input().split()
    ism = satr[0]
    baho = int(satr[1])
    talabalar.append((ism, baho))
    
talabalar.sort(key=lambda x: (-x[1], x[0]))

for ism, baho in talabalar:
    print(f"{ism} {baho}")