n = int(input())
mah = {}
for _ in range(n):
    nomi, narx = input().split()
    mah[nomi] = int(narx)
    
print(sum(mah.values()))