# O'rtacha og'irligi
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
numbers = [a, b, c, d, e]
filtered_sum = sum(numbers) - max(numbers) - min(numbers)
result = filtered_sum // 3
print(result)