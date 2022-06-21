n = int(input())

s = 1





for i in range (n * 2):

    print(f"{s} {s**2 + (i%2)} {s ** 3 + (i%2)}")

    s += (i%2)
