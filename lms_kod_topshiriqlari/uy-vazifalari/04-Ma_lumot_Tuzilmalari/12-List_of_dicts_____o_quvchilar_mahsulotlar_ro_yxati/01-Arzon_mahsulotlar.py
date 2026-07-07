n = int(input())
mah = []
for _ in range(n):
    nomi, narxo = input().split()
    mah.append({"nomi": nomi, "narxo": int(narxo)})
cheg = int(input())
for mahs in mah:
    if mahs["narxo"] < cheg:
        print(mahs["nomi"])