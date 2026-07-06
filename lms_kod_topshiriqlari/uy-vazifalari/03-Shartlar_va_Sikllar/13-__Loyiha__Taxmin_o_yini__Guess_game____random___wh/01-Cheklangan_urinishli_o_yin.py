yash = int(input())
n = int(input())
topild = False
for _ in range(n):
    tax = int(input())
    if tax == yash:
        print("TOPDINGIZ")
        topild = True
        break
    elif tax < yash:
        print("KICHIK")
    else:
        print("KATTA")
if not topild:
    print("YUTQAZDINGIZ")