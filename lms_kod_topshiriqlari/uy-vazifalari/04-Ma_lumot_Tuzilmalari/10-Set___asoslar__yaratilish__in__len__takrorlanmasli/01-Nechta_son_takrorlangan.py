sonlar = input().split()
seen = set()
dups = set()
for u in sonlar:
    if u in seen:
        dups.add(u)
    else:
        seen.add(u)
print(len(dups))