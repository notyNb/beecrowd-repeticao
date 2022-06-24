t = int(input())



for i in range(0,t):
    ordem = input().split()
    pa = int(ordem[0])
    pb = int(ordem[1])
    g1 = float(ordem[2])/ 100
    g2 = float(ordem[3])/ 100

    anos = 0

    while True:
        pa += int(g1 * pa)
        pb += int(g2 * pb)
        anos += 1

        if pa > pb or anos > 100:
            break
    
    if anos <= 100:
        print(f"{anos} anos.")
    else:
        print("Mais de 1 seculo.")
