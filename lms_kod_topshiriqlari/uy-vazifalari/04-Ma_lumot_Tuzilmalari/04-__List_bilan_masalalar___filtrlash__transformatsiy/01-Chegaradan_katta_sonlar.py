sonlar = list(map(int, input().split()))
cheqara = int(input())
katta = [son for son in sonlar if son > cheqara]
print(' '.join(map(str, katta)))