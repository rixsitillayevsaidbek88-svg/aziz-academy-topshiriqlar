n = int(input())
uc = 0
for _ in range(n):
    son = int(input())
    if son % 3 == 0:
        uc += 1
print(uc)