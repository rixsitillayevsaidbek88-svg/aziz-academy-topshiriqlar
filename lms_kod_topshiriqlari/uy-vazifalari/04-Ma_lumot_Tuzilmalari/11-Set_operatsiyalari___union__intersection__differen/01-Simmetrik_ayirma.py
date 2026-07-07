a = set(map(int, input().split()))
b = set(map(int, input().split()))
sim = sorted(a ^ b)
print(*sim)