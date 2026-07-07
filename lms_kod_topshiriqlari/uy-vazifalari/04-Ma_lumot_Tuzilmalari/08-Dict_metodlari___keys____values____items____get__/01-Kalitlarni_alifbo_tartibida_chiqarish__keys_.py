n = int(input())
tala = {}
for _ in range(n):
    ism, baho = input().split()
    tala[ism] = baho
sara = sorted(tala.keys())
print(*sara)