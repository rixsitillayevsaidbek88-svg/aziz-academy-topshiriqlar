a = set(map(int, input().split()))
b = set(map(int, input().split()))
ayir = sorted(a - b)
print(*ayir)