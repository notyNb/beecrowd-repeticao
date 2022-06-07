x = int(input())
y = int(input())
soma = 0
f = 0

for i in range(y+1, x):
    if x == y:
        print(0)
    elif i % 2 != 0:
        soma += i
    else:
        f += 1

print(soma)
