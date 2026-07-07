sozlar = input().split()
freq = {}
for soz in sozlar:
    freq[soz] = freq.get(soz, 0) + 1
n = len(freq)
print(n)