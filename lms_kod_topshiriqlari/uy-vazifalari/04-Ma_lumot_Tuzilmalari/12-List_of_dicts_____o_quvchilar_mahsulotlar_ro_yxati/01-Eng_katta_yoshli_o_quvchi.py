n = int(input())
ro = []
for _ in range(n):
    ism, yosh = input().split()
    ro.append({"ism": ism, "yosh": int(yosh)})
    
eng = max(ro, key=lambda x: x["yosh"])
print(eng["ism"])