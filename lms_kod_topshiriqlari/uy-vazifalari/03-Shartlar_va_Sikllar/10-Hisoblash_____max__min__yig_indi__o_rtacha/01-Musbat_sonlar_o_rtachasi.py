n = int(input())
musbaty = 0
musbat = 0
for _ in range(n):
    son = int(input())
    if son > 0:
        musbaty += son
        musbat += 1
if musbat == 0:
    print(0)
else:
    orta = musbaty // musbat
    print(orta)