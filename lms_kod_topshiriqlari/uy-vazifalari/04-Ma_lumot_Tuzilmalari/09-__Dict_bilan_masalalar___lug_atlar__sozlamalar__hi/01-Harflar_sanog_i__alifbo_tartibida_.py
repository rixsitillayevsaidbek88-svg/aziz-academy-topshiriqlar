soz = input()
freq = {}
for harf in soz:
    freq[harf] = freq.get(harf, 0) + 1
for harf, son in sorted(freq.items()):
    print(f"{harf} {son}")