# Davomat tahlili
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
attendance = input().split()
attended_days = attendance.count('1')
max_streak = 0
current_streak = 0
for day in attendance:
    if day == '1':
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0
percentage = (attended_days * 100) // n
print(attended_days)
print(max_streak)
print(percentage)