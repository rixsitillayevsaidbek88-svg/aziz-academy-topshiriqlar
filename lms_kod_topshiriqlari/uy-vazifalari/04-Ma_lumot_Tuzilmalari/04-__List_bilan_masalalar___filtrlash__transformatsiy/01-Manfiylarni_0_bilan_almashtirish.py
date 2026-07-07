nums = list(map(int, input().split()))
nolga = [num if num >= 0 else 0 for num in nums]
print(' '.join(map(str, nolga)))