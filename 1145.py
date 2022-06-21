x, y = map(int, input().split())
limite = 1

for i in range (1, y+1):
    if (limite==x):    
        print(i)
        limite=1
    else:
        print(i, end=" ")
        limite+= 1
