yigindi = 0
while True:
    son = int(input())
    if son < 0:
        continue
    if son >= 100:
        break
        
    if son == 0:
        break
    yigindi += son
print(yigindi)