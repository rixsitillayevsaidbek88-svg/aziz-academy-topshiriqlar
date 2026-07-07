set1 = set(input().split())
set2 = set(input().split())
print(sum(1 for x in set1 if x in set2))