n = int(input())
mahsu = {}
for _ in range(n):
    nomi, soni = input().split()
    mahsu[nomi] = soni
    
qid = input()
print(mahsu.get(qid, "Topilmadi"))