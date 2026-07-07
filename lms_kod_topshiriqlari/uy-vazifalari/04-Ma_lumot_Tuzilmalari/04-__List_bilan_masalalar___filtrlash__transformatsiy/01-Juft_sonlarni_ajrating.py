a = list(map(int, input().split()))
juft = [num for num in a if num % 2 == 0]
print(' '.join(map(str, juft)))