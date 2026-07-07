n = int(input())
royhat = []
for _ in range(n):
    ism, mat, fiz = input().split()
    royhat.append({"ism": ism, "mat": int(mat), "fiz": int(fiz)})
    
for oquvchi in royhat:
    jami = oquvchi["mat"] + oquvchi["fiz"]
    print(oquvchi["ism"], jami)