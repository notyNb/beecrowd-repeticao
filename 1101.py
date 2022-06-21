while True:
    linha = input().split()

    m = int(linha[0])
    n = int(linha[1])
    sum = 0


    if n <= 0:
        break
    elif m <= 0:
        break

    if m > n:
        for i in range(n, m+1):
            sum += i
            print(i, end=" ", )
        print(f"Sum={sum}")

    else:
        for i in range(m, n+1):
            sum += i
            print(i, end=" ", )
        print(f"Sum={sum}")
