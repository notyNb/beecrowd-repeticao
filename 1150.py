x = int(input())

maiorZ = 0
menorZ = 0
soma = 0
digitos = 0

for i in range(x):
    z = int(input())
    if z <= x:
        menorZ += 1
    else:
        maiorZ = z
        break

for j in range(x, maiorZ+1):
    soma += j
    digitos += 1
    if soma > maiorZ:
        break

    
print(digitos)
