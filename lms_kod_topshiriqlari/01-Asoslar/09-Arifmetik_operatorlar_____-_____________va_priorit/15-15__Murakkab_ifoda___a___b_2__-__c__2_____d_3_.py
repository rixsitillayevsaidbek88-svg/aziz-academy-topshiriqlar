a, b, c, d = map(int, input().split())
n = (a+b*2) - (c//2) + (d%3)
print(f"Result: {n}")