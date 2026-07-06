r = int(input())
jami = 0
eng = float('inf')
for i in range(1, r + 1):
    yash = int(input())
    bos = 0
    
    while True:
        tax = int(input())
        bos += 1
        
        if tax == yash:
            break
    print(f"Round {i}: {bos} urinish")
    jami += bos
    if bos < eng:
        eng = bos
print(f"Jami: {jami}")
print(f"Eng yaxshi: {eng}")