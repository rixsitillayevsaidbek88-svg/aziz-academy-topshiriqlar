# Kafe: kunlik hisobot
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
total_revenue = 0
total_count = 0
max_revenue = -1
best_dish = ""
for _ in range(n):
    line = input().split()
    name = line[0]
    price = int(line[1])
    quantity = int(line[2])
    current = price * quantity
    total_revenue += current
    total_count += quantity
    
    if current > max_revenue:
        max_revenue = current
        best_dish = name
print(total_revenue)
print(best_dish)
print(total_count)