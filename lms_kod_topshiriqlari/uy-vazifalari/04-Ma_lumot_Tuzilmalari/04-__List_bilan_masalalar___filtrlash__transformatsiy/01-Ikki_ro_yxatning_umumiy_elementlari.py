a1 = input().split()
a2 = input().split()
print(*(x for x in dict.fromkeys(a1) if x in a2))