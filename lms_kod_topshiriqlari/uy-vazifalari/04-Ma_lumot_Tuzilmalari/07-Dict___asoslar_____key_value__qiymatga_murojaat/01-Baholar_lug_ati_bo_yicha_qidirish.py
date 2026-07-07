n = int(input())
baholar = {}
for _ in range(n):
    ism, baho = input().split()
    baholar[ism] = baho
qid = input()
print(baholar[qid])