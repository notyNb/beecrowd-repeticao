dentro = 0
fora = 0

for i in range(int(input())):
    a = int(input())

    if a>=10 and a<=20:
        dentro += 1

    else:
        fora += 1


print(f"{dentro} in")
print(f"{fora} out")
