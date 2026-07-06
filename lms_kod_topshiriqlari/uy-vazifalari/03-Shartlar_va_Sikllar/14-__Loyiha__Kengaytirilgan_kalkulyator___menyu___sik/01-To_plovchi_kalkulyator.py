natija = 0
while True:
    belgi = input()
    if belgi == "=":
        break
    son = int(input())
    if belgi == "+":
        natija += son
    elif belgi == "-":
        natija -= son
    elif belgi == "*":
        natija *= son
    elif belgi == "/":
        natija //= son
print(natija)