yash = int(input())
tax = int(input())
for _ in range(tax):
    taxmin = int(input())
    if taxmin == yash:
        print("TOPDINGIZ")
    elif taxmin > yash:
        print("KATTA")
    else:
        print("KICHIK")