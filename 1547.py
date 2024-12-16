m = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(m)]
x = 1

for x1, x2 in pairs: 
        if x == x1: 
                x = x2
        elif x == x2: 
                x = x1 

print(x)
