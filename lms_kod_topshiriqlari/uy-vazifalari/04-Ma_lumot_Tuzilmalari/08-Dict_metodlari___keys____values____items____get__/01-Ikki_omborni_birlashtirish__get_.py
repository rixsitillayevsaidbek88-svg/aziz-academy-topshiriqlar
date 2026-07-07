n = int(input())
total = {}
for _ in range(n):
    mahsulot, miqdor = input().split()
    miqdor = int(miqdor)
    total[mahsulot] = total.get(mahsulot, 0) + miqdor
    
m = int(input())
for _ in range(m):
    mahsulot, miqdor = input().split()
    miqdor = int(miqdor)
    total[mahsulot] = total.get(mahsulot, 0) + miqdor
    
for mahsulot, miqdor in sorted(total.items()):
    print(f"{mahsulot} {miqdor}")