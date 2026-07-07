a = set(map(int, input().split()))
b = set(map(int, input().split()))
ks = sorted(a & b)
print(*ks)