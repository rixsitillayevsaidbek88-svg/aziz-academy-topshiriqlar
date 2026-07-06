n = int(input())
eng = int(input())
for _ in range(n - 1):
    son = int(input())
    if son > eng:
        eng = son
print(eng)