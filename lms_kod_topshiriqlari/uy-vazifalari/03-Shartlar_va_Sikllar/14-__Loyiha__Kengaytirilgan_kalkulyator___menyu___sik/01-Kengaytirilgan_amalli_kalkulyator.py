engk = float('-inf')
while True:
    amal = int(input())
    if amal == 0:
        break
    a, b = int(input()), int(input())
    res = None
    if amal == 1: res = a + b
    elif amal == 2: res = a - b
    elif amal == 3: res = a * b
    elif amal == 5: res = a ** b
    elif b != 0:
        if amal == 4: res = a // b
        elif amal == 6: res = a % b
    if res is not None:
        print(res)
        if res > engk:
            engk = res
print(f"Eng katta natija: {engk}")
    