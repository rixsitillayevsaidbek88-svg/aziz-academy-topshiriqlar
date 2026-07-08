n = int(input())
for _ in range(n):
    data = input().split()
    name = data[0]
    total = sum(map(int, data[1:]))
    
    print(f"{name} {total}")