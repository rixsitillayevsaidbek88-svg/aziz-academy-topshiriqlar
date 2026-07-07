sonlar = list(map(int, input().split()))
freq = {}
for son in sonlar:
    freq[son] = freq.get(son, 0) + 1
    
max_freq = max(freq.values())
eng = min([son for son, freq in freq.items() if freq == max_freq])
print(eng)