a = list(map(int, input().split()))
copy  = a[:]
copy.sort()
print(' '.join(map(str, a)))
print(' '.join(map(str, copy)))