n = int(input())
yoshl = 0
for _ in range(n):
    malu = input().split()
    ism = malu[0]
    yosh = int(malu[1])
    
    oqi = {"ism": ism, "yosh": yosh}
    yoshl += oqi["yosh"]
    
print(yoshl)