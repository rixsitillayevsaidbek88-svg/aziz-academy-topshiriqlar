n = int(input())
engk = engkk = int(input())
for _ in range(n - 1):
    son = int(input())
    if son > engk:
        engk = son
    elif son < engkk:
        engkk = son
farq = engk - engkk
print(farq)