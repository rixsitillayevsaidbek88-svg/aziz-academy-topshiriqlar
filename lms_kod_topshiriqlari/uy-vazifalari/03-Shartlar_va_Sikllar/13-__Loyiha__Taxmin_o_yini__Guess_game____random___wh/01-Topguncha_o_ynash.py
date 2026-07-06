yashrin = int(input())
urinish = 0
while True:
    tax = int(input())        
    urinish += 1
    if tax == yashrin:
        print("TOPDINGIZ")
        break
    elif tax > yashrin:
        print("KATTA")
    else:
        print("KICHIK")
        
print(f"Urinishlar: {urinish}")