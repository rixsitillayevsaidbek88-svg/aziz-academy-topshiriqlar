n = int(input())
tub_son = []
for num in range(2, n + 1):
    count = 0
    for i in range(1, n + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        tub_son.append(num)
print(*tub_son)