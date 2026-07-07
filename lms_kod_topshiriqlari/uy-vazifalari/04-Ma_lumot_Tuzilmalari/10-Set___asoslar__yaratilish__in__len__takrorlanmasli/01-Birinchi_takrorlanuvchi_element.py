sonlar = input().split()
seen = set()
topild = False
for u in sonlar:
    if u in seen:
        print(u)
        topild = True
        break
    else:
        seen.add(u)
        
if not topild:
    print("Yo'q")