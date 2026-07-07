n = int(input())
total = {}
for _ in range(n):
    gruh, ball = input().split()
    ball = int(ball)
    total[gruh] = total.get(gruh, 0) + ball
    
for gruh, yigindi in sorted(total.items()):
    print(f"{gruh} {yigindi}")