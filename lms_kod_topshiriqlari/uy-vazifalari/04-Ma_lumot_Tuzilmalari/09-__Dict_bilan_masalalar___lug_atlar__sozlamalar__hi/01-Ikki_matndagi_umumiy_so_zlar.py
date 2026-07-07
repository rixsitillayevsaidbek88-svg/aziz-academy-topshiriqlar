sozlar1 = input().split()
sozlar2 = input().split()
umumiy = {}
for soz in sozlar1:
    umumiy[soz] = 1
    
umumiy2 = {}
for soz in sozlar2:
    if soz in umumiy and soz not in umumiy2:
        umumiy2[soz] = 1
        
umumiy = sorted(umumiy2.keys())
for soz in umumiy:
    print(soz)