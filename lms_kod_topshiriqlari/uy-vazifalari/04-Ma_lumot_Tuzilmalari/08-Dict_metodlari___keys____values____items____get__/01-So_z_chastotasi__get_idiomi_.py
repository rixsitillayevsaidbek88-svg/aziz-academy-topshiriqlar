sozlar = input().split()
freq = {}
for soz in sozlar:
    freq[soz] = freq.get(soz, 0) + 1
soz_soni = sorted(freq.items(), key=lambda x: x[0])
print(*[f"{soz} {soni}" for soz, soni in soz_soni], sep='\n')