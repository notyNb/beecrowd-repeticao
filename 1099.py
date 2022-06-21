n = int(input())

for i in range(n):
    linha = input().split()

    x = int(linha[0])
    y = int(linha[1])

    soma = 0

    if x < y:
        for num in range (x+1, y, 1):
            if num % 2 != 0:
                soma += num
        
        print(f"{soma}")

    else:
        for num in range (x-1, y, -1):
            if num % 2 != 0:
                soma += num

        print(f"{soma}")
