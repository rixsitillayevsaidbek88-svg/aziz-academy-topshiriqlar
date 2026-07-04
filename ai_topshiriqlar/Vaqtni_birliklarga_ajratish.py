# Vaqtni birliklarga ajratish
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

t = int(input())
days = t // 86400
remainder = t % 86400
hours = remainder // 3600
remainder = remainder % 3600
minutes = remainder // 60
seconds = remainder % 60
print(days)
print(hours)
print(minutes)
print(seconds)