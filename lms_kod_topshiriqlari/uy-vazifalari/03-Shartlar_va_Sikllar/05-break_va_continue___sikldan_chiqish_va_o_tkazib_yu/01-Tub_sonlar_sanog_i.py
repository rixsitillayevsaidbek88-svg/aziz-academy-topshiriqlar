tub_sonlar = 0
while True:
    son = int(input())
    if son == 0:
        break
        
    if son < 2:
        continue
        
    bo_luvchi = 2
    is_prime = True
    
    while bo_luvchi * bo_luvchi <= son:
        if son % bo_luvchi == 0:
            is_prime = False
            break
        bo_luvchi += 1
        
    if is_prime:
        tub_sonlar += 1

print(tub_sonlar)