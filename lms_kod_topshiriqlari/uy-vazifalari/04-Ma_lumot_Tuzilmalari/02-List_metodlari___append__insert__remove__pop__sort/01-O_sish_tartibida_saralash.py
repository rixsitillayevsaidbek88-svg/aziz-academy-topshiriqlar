n = int(input())
sonlar = []
for _ in range(n):
    sonlar.append(int(input()))
    
sonlar.sort()
print(*sonlar)