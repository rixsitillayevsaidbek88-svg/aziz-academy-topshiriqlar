# Yakuniy reyting
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
ishtirokchilar = []
jami_ball = 0
for i in range(n):
    ism, ball_str = input().split()
    ball = int(ball_str)
    
    ishtirokchilar.append((ism, ball))
    jami_ball += ball

ortacha_butun = jami_ball // n


golib_ismi = ""
maks_ball = -1

for ism, ball in ishtirokchilar:
    if ball > maks_ball:
        maks_ball = ball
        golib_ismi = ism
    elif ball == maks_ball:
        if ism < golib_ismi:
            golib_ismi = ism
yuqori_sanoq = 0
for ism, ball in ishtirokchilar:
    if ball > ortacha_butun:
        yuqori_sanoq += 1

print(golib_ismi)
print(ortacha_butun)
print(yuqori_sanoq)