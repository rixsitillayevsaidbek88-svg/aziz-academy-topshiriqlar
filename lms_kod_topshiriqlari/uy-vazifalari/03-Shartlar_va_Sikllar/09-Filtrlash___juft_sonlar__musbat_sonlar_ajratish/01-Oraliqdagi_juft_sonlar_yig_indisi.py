a = int(input())
b = int(input())
juft = 0
for son in range(a, b + 1):
    if son % 2 == 0:
        juft += son
print(juft)